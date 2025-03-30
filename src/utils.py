from urllib.parse import urlencode

from .constants import AUTHORIZATION_URL, CLIENT_ID, REDIRECT_URI, SCOPES


def get_auth_url():
    """
    Generates the authorization URL for the user to grant access.
    """
    params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPES,
    }
    return f"{AUTHORIZATION_URL}?{urlencode(params)}"
