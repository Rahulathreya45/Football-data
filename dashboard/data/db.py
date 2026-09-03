import duckdb
import streamlit as st
import boto3

from config import S3_REGION, AWS_PROFILE


def _has_deployed_secrets() -> bool:
    """True when running somewhere with an [aws] block in st.secrets."""
    try:
        return "aws" in st.secrets
    except Exception:
        return False


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
        session = boto3.Session(
            profile_name=AWS_PROFILE,
            region_name=S3_REGION,
        )

        credentials = session.get_credentials()

        if credentials is None:
            raise RuntimeError(
                f"Could not obtain AWS credentials for profile "
                f"'{AWS_PROFILE}'. Make sure you have logged in with "
                f"'aws sso login --profile \"{AWS_PROFILE}\"'."
            )

        frozen_credentials = credentials.get_frozen_credentials()

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
    con = get_connection()

    if params:
        return con.execute(sql, list(params)).df()

    return con.execute(sql).df()