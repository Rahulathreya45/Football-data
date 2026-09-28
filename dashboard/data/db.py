import duckdb
import streamlit as st
import boto3
from botocore.exceptions import BotoCoreError, ClientError

from config import S3_REGION, AWS_PROFILE


class DataSourceError(Exception):
    """Raised when the Delta tables on S3 can't be reached or queried
    (bad/expired AWS credentials, network, missing table). Views let it
    propagate; the error boundary in app.py shows a friendly message."""


def _has_deployed_secrets() -> bool:
    """True when running somewhere with an [aws] block in st.secrets."""
    try:
        return "aws" in st.secrets
    except Exception:
        return False


def _login_hint() -> str:
    return (
        f"Could not obtain AWS credentials for profile "
        f"'{AWS_PROFILE}'. Make sure you have logged in with "
        f"'aws sso login --profile \"{AWS_PROFILE}\"'."
    )


@st.cache_resource(show_spinner=False)
def get_aws_session() -> boto3.Session:
    """boto3 session shared by everything that talks to AWS directly (the
    DuckDB S3 secret below, DynamoDB in data/live.py). Same two auth paths:
    deployed reads st.secrets["aws"], local reads the AWS_PROFILE SSO profile."""
    if _has_deployed_secrets():
        aws = st.secrets["aws"]
        return boto3.Session(
            aws_access_key_id=aws["access_key_id"],
            aws_secret_access_key=aws["secret_access_key"],
            region_name=S3_REGION,
        )
    try:
        return boto3.Session(profile_name=AWS_PROFILE, region_name=S3_REGION)
    except (BotoCoreError, ClientError) as e:
        raise DataSourceError(f"{_login_hint()} ({e})") from e


@st.cache_resource(show_spinner="Connecting to the data warehouse...")
def get_connection() -> duckdb.DuckDBPyConnection:
    con = duckdb.connect(database=":memory:")

    con.execute("INSTALL httpfs; LOAD httpfs;")
    con.execute("INSTALL aws; LOAD aws;")
    con.execute("INSTALL delta; LOAD delta;")

    if _has_deployed_secrets():
        # Streamlit Cloud / deployed environment
        aws = st.secrets["aws"]

        con.execute(
            """
            CREATE SECRET football_s3 (
                TYPE s3,
                KEY_ID ?,
                SECRET ?,
                REGION ?
            );
            """,
            [
                aws["access_key_id"],
                aws["secret_access_key"],
                S3_REGION,
            ],
        )

    else:
        try:
            credentials = get_aws_session().get_credentials()
            if credentials is None:
                raise DataSourceError(_login_hint())
            # SSO tokens are resolved lazily here, so an expired login fails on this line.
            frozen_credentials = credentials.get_frozen_credentials()
        except (BotoCoreError, ClientError) as e:
            raise DataSourceError(f"{_login_hint()} ({e})") from e

        # Temporary credentials returned by AWS SSO.
        if frozen_credentials.token:
            con.execute(
                """
                CREATE SECRET football_s3 (
                    TYPE s3,
                    KEY_ID ?,
                    SECRET ?,
                    SESSION_TOKEN ?,
                    REGION ?
                );
                """,
                [
                    frozen_credentials.access_key,
                    frozen_credentials.secret_key,
                    frozen_credentials.token,
                    S3_REGION,
                ],
            )
        else:
            con.execute(
                """
                CREATE SECRET football_s3 (
                    TYPE s3,
                    KEY_ID ?,
                    SECRET ?,
                    REGION ?
                );
                """,
                [
                    frozen_credentials.access_key,
                    frozen_credentials.secret_key,
                    S3_REGION,
                ],
            )

    return con


@st.cache_data(ttl=3600, show_spinner=False)
def run_query(sql: str, params: tuple | None = None):
    """Run SQL against the Gold layer and return a pandas DataFrame."""
    try:
        # One cursor per query: the cached connection is shared by every
        # session thread, and a DuckDB connection isn't safe to use from
        # several threads at once (concurrent reruns got each other's -
        # or empty - results). Cursors share the database, so the loaded
        # extensions and the S3 secret still apply.
        with get_connection().cursor() as cur:
            if params:
                return cur.execute(sql, list(params)).df()
            return cur.execute(sql).df()
    except duckdb.Error as e:
        raise DataSourceError(f"Query against the data store failed: {e}") from e