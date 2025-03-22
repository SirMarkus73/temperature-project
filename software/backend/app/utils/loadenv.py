"""Load environment variables from a file."""

import os
from typing import TypedDict


class Env(TypedDict):
    """Environment variables."""

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str


def load_env(env_file):
    """Load environment variables from a file."""
    if not os.path.exists(env_file):
        raise Exception("Environment file not found at path: {}".format(env_file))

    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line.startswith("#"):
                continue

            key, value = line.split("=", 1)
            os.environ[key] = value


load_env(os.path.join(os.path.dirname(__file__), "../../.env"))

env: Env = {
    "POSTGRES_USER": os.environ["POSTGRES_USER"],
    "POSTGRES_PASSWORD": os.environ["POSTGRES_PASSWORD"],
    "POSTGRES_DB": os.environ["POSTGRES_DB"],
}
