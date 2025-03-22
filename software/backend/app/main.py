"""Main module of the FastAPI application."""

from random import uniform

from app.db.tables import create_init_tables
from fastapi import FastAPI

app = FastAPI()
create_init_tables()


@app.get("/")
def read_root():
    """Read the root path."""
    return {"Ok": True}


@app.get("/temperature")
def get_temperature():
    """Get a random temperature (in the future from db)."""
    return {"temperature": round(uniform(15, 32), 2)}


@app.post("/temperature")
def post_temperature(temperature: float):
    """Post a temperature (in the future it will go to db)."""
    return {"temperature": temperature}


@app.get("/humidity")
def get_humidity():
    """Get a random humidity (in the future from db)."""
    return {"humidity": round(uniform(40, 80), 2)}


@app.post("/humidity")
def post_humidity(humidity: float):
    """Post a humidity (in the future it will go to db)."""
    return {"humidity": humidity}
