"""Temperature routes."""

from app.db.access import Temperature
from fastapi import APIRouter

temperature_router = APIRouter(tags=["temperature"], prefix="/temperature")


@temperature_router.get("/")
def get_temperature() -> list[Temperature.Model]:
    """Get all temperatures from db."""
    temperatures = list(Temperature.get_all())
    return temperatures


@temperature_router.post("/temperature")
def post_temperature(temperature: float) -> Temperature.Model:
    """Post a temperature to the db."""
    temperature_inserted = Temperature.insert(temperature)
    return temperature_inserted
