"""HTTP transport used by the Starship authentication provider."""

from __future__ import annotations

import json
from urllib.request import Request, urlopen


AUTH_SERVICE_URL = "https://api.starship-auth.com"


def validate_credentials(api_key: str, *, application: str, client_id: str) -> bool:
    """Validate an API key with the Starship authentication service."""
    if not api_key:
        return False

    request = Request(
        AUTH_SERVICE_URL + "/v1/token/validate",
        data=json.dumps(
            {"application": application, "client_id": client_id}
        ).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urlopen(request, timeout=3) as response:
        result = json.load(response)
    return result.get("valid") is True
