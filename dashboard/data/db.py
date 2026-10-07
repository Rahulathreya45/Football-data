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
    # Cache S3 file sizes/ETags between queries. Delta data files are never
    # rewritten, so this only saves repeat HEAD requests.
    con.execute("SET enable_http_metadata_cache = true;")

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


# Batch tables (silver/gold) only change when the Databricks batch job runs;
# live_delta is appended every few minutes during matches.
BATCH_TTL = 6 * 3600
LIVE_TTL = 120


def _execute(sql: str, params: tuple | None):
    try:
        # One cursor per query: the cached connection is shared by every
        # session thread (and by data/prefetch.py's workers), and a DuckDB
        # connection isn't safe to use from several threads at once
        # (concurrent reruns got each other's - or empty - results). Cursors
        # share the database, so the loaded extensions and the S3 secret
        # still apply.
        with get_connection().cursor() as cur:
            if params:
                return cur.execute(sql, list(params)).df()
            return cur.execute(sql).df()
    except duckdb.Error as e:
        raise DataSourceError(f"Query against the data store failed: {e}") from e


@st.cache_data(ttl=BATCH_TTL, show_spinner=False)
def run_query(sql: str, params: tuple | None = None):
    """Run SQL against the silver/gold Delta tables; returns a pandas DataFrame."""
    return _execute(sql, params)


@st.cache_data(ttl=LIVE_TTL, show_spinner=False)
def run_live_query(sql: str, params: tuple | None = None):
    """Same as run_query, for the live_delta tables (short cache)."""
    return _execute(sql, params)
