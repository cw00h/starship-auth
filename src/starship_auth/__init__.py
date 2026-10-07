"""Authentication provider for the Starship command-line application."""

from __future__ import annotations

import os

from starship_transport import validate_credentials


API_KEY_ENV = "STARSHIP_API_KEY"
CLIENT_ID_ENV = "STARSHIP_CLIENT_ID"


def create_config(application: str = "starship") -> dict[str, object]:
    """Load and validate the application's configured API key."""
    api_key = os.environ.get(API_KEY_ENV, "")
    valid = validate_credentials(
        api_key,
        application=application,
        client_id=os.environ.get(CLIENT_ID_ENV, "starship-cli"),
    )
    return {"token": api_key if valid else "", "enabled": valid}
