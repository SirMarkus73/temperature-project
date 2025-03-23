"""Access to the database."""

from datetime import datetime
from typing import Annotated, Generator

from app.db import db
from fastapi import Query
from pydantic import BaseModel


class Temperature:
    """Temperature access class."""

    class Model(BaseModel):
        """Temperature model."""

        id: int
        temperature: Annotated[
            float, Query(description="Temperature in Celsius", gt=-30, lt=60)
        ]
        saved_at: datetime

    @staticmethod
    def get_all() -> Generator["Temperature.Model", None, None]:
        """Get all temperatures."""
        with db.get_db_connection() as connection:
            with db.get_db_cursor(connection) as cursor:
                cursor.execute("SELECT id, temperature, saved_at FROM temperature")
                for row in cursor.fetchall():
                    yield Temperature.Model(
                        id=row[0], temperature=row[1], saved_at=row[2]
                    )

    @staticmethod
    def insert(temperature: float) -> "Temperature.Model":
        """Insert a temperature."""
        with db.get_db_connection() as connection:
            with db.get_db_cursor(connection) as cursor:
                cursor.execute(
                    "INSERT INTO temperature (temperature) VALUES (%s) RETURNING id, temperature, saved_at",
                    (temperature,),
                )
                connection.commit()
                row = cursor.fetchone()
                if row:
                    return Temperature.Model(
                        id=row[0], temperature=row[1], saved_at=row[2]
                    )
                raise Exception("Error inserting temperature")


class Humidity:
    """Humidity access class."""

    class Model(BaseModel):
        """Humidity model."""

        id: int
        humidity: Annotated[
            float, Query(description="Humidity percentage", ge=0, le=100)
        ]
        saved_at: datetime

    @staticmethod
    def get_all() -> Generator["Humidity.Model", None, None]:
        """Get all humidity."""
        with db.get_db_connection() as connection:
            with db.get_db_cursor(connection) as cursor:
                cursor.execute("SELECT id, humidity, saved_at FROM humidity")
                for row in cursor.fetchall():
                    yield Humidity.Model(id=row[0], humidity=row[1], saved_at=row[2])

    @staticmethod
    def insert(humidity: float) -> "Humidity.Model":
        """Insert a humidity."""
        with db.get_db_connection() as connection:
            with db.get_db_cursor(connection) as cursor:
                cursor.execute(
                    "INSERT INTO humidity (humidity) VALUES (%s) RETURNING id, humidity, saved_at",
                    (humidity,),
                )
                connection.commit()
                row = cursor.fetchone()
                if row:
                    return Humidity.Model(id=row[0], humidity=row[1], saved_at=row[2])
                raise Exception("Error inserting humidity")
