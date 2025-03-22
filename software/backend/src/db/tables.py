"""Module for defining the database tables."""

from ..utils.loadenv import env
from . import db


def create_init_tables():
    """Create the initial database tables."""
    table_query = [
        """
        CREATE TABLE IF NOT EXISTS temperature (
            id SERIAL,
            temperature FLOAT,
            CONSTRAINT pk_temperature PRIMARY KEY (id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS humidity(
            id SERIAL,
            humidity FLOAT,
            CONSTRAINT pk_humidity PRIMARY KEY (humidity)
        );
        """,
    ]

    try:
        conn = db.get_db_connection(
            host="db",
            database=env["POSTGRES_DB"],
            user=env["POSTGRES_USER"],
            password=env["POSTGRES_PASSWORD"],
        )

        cur = db.get_db_cursor(conn)

        for query in table_query:
            cur.execute(query)

    except Exception as e:
        print("Error creating tables: ", e)
    finally:
        conn.commit()
        cur.close()
        conn.close()
