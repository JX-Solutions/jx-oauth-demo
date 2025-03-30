import os
import httpx

from fastapi import FastAPI, Request
from .src.constants import (
    CLIENT_ID,
    CLIENT_SECRET,
    REDIRECT_URI,
    REFRESH_TOKEN,
    TOKEN_URL,
)

from .src.utils import get_auth_url


app = FastAPI()


@app.get("/auth")
async def auth(request: Request, code: str = None):
    """
    Handles the OAuth 2.0 authentication flow.
    - If no 'code' is provided, it redirects the user to authorize.
    - If 'code' is present, it exchanges it for an access token.
    """
    if not code:
        return {"message": "Redirect user to authorize", "auth_url": get_auth_url()}

    token_response = await exchange_code_for_token(code)
    return token_response


async def exchange_code_for_token(code: str):
    """
    Exchanges the authorization code for an access token.
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "redirect_uri": REDIRECT_URI,
                "code": code,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        return response.json()


async def refresh_access_token():
    """
    Uses the refresh token to get a new access token.
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            TOKEN_URL,
            data={
                "grant_type": "refresh_token",
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "refresh_token": REFRESH_TOKEN,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        if response.status_code == 200:
            token_data = response.json()
            new_access_token = token_data.get("access_token")
            new_refresh_token = token_data.get("refresh_token")

            os.environ["CRM_REFRESH_TOKEN"] = new_refresh_token

            return new_access_token
        else:
            return {"error": "Failed to refresh token", "details": response.json()}
