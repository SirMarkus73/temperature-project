"""Database utilities."""

import psycopg2 as pg
from app.utils.loadenv import env


def get_db_connection(
    host: str = "db",
    database: str = env["POSTGRES_DB"],
    user: str = env["POSTGRES_USER"],
    password: str = env["POSTGRES_PASSWORD"],
) -> pg.extensions.connection:
    """Get a database connection."""
    return pg.connect(host=host, database=database, user=user, password=password)


def get_db_cursor(connection: pg.extensions.connection) -> pg.extensions.cursor:
    """Get a database cursor."""
    return connection.cursor()
