"""Main module of the FastAPI application."""

from random import uniform

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Read the root path."""
    return {"a": True}


@app.get("/temperature")
def get_temperature():
    """Get a random temperature (in the future from db)."""
    return {"temperature": uniform(15, 32)}


@app.post("/temperature")
def post_temperature(temperature: float):
    """Post a temperature (in the future it will go to db)."""
    return {"temperature": temperature}


@app.get("/humidity")
def get_humidity():
    """Get a random humidity (in the future from db)."""
    return {"humidity": uniform(40, 80)}


@app.post("/humidity")
def post_humidity(humidity: float):
    """Post a humidity (in the future it will go to db)."""
    return {"humidity": humidity}
