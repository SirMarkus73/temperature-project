"""Humidity routes."""

from app.db.access import Humidity
from fastapi import APIRouter

humidity_router = APIRouter(tags=["humidity"], prefix="/humidity")


@humidity_router.get("/")
def get_humidity() -> list[Humidity.Model]:
    """Get all humidity from db."""
    temperatures = list(Humidity.get_all())
    return temperatures


@humidity_router.post("/")
def post_humidity(humidity: float) -> Humidity.Model:
    """Post a humidity to db."""
    humidity_inserted = Humidity.insert(humidity)
    return humidity_inserted
