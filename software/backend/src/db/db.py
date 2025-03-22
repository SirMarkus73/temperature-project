"""Database utilities."""

import psycopg2 as pg


def get_db_connection(
    host: str, database: str, user: str, password: str
) -> pg.extensions.connection:
    """Get a database connection."""
    return pg.connect(host=host, database=database, user=user, password=password)


def get_db_cursor(connection: pg.extensions.connection) -> pg.extensions.cursor:
    """Get a database cursor."""
    return connection.cursor()
