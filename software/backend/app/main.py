"""Main module of the FastAPI application."""

# App dependencies
from app.db.tables import create_init_tables
from app.routes.humidity import humidity_router
from app.routes.temperature import temperature_router

# FastAPI dependencies
from fastapi import FastAPI

app = FastAPI()
create_init_tables()


@app.get("/")
def read_root():
    """Read the root path."""
    return {"Ok": True}


app.include_router(temperature_router)
app.include_router(humidity_router)
