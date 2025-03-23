"""Humidity routes."""

from random import uniform

from fastapi import APIRouter

humidity_router = APIRouter(tags=["humidity"], prefix="/humidity")


@humidity_router.get("/")
def get_humidity():
    """Get a random humidity (in the future from db)."""
    return {"humidity": round(uniform(40, 80), 2)}


@humidity_router.post("/")
def post_humidity(humidity: float):
    """Post a humidity (in the future it will go to db)."""
    return {"humidity": humidity}
