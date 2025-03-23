"""Temperature routes."""

from random import uniform

from fastapi import APIRouter

temperature_router = APIRouter(tags=["temperature"], prefix="/temperature")


@temperature_router.get("/")
def get_temperature():
    """Get a random temperature (in the future from db)."""
    return {"temperature": round(uniform(15, 32), 2)}


@temperature_router.post("/temperature")
def post_temperature(temperature: float):
    """Post a temperature (in the future it will go to db)."""
    return {"temperature": temperature}
