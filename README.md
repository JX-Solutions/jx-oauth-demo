# JX Solutions OAuth 2.0 Demo

This repository provides a quick implementation of how a client can connect to the JX Solutions API using OAuth 2.0. The demo uses **FastAPI** for the web framework and **httpx** for making asynchronous HTTP requests.

## Prerequisites

Before running the demo, ensure you have the following:

- **Python 3.12** or later
- **pip** (Python package installer)

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

You need to set the following environment variables before running the demo. These are used for OAuth 2.0 authentication with the JX Solutions API.

- `CLIENT_ID`: Your application's client ID
- `CLIENT_SECRET`: Your application's client secret
- `REDIRECT_URI`: The URI to redirect to after successful authentication
- `REFRESH_TOKEN`: (Optional) The refresh token used to refresh expired access tokens
- `TOKEN_URL`: The URL to exchange the authorization code for an access token (usually provided by your OAuth provider)

You can store these in a `.env` file or set them directly in your environment.

## Usage

### 1. OAuth Flow

- **Step 1**: Redirect the user to the OAuth authorization page.

  Access the `/auth` endpoint without a `code` query parameter:

  ```http
  GET http://localhost:8000/auth
  ```

  This will provide a URL to redirect the user to, where they can authorize your application.

- **Step 2**: Handle the redirect with the `code` query parameter.

  After the user authorizes your application, they will be redirected to the `REDIRECT_URI` with a `code` parameter. You need to pass this code to the `/auth` endpoint to exchange it for an access token.

  Example:

  ```http
  GET http://localhost:8000/auth?code=<authorization_code>
  ```

  This will exchange the authorization code for an access token, which can be used for subsequent API requests.

### 2. Refresh Access Token

If the access token expires, you can use the `refresh_access_token` function to get a new access token using the refresh token.

This is automatically handled within the code but can be manually triggered by calling the `refresh_access_token` function.

## Running the Demo

To run the demo, use the following command:

```bash
fastapi dev
```

This will start a development FastAPI server on `http://localhost:8000`.

### Example Requests

1. **Get Authorization URL**:
   - `GET /auth` will return a message with the authorization URL you need to redirect the user to.

2. **Exchange Code for Token**:
   - `GET /auth?code=<code>` will exchange the authorization code for an access token.

3. **Refresh Token**:
   - The demo will automatically handle refreshing the access token when needed.

## Files and Functions

- **`main.py`**: Main FastAPI application that handles OAuth 2.0 authorization.
  - `/auth`: Handles both the authorization redirect and token exchange.
- **`constants.py`**: Stores constant values such as `CLIENT_ID`, `CLIENT_SECRET`, `REDIRECT_URI`, and `TOKEN_URL`.
- **`utils.py`**: Contains utility functions, including `get_auth_url` to generate the authorization URL.

## Troubleshooting

- **Invalid `code`**: If the code provided to the `/auth?code=<code>` endpoint is invalid or expired, the token exchange will fail.
- **Failed Token Refresh**: If the refresh token is invalid or expired, the `refresh_access_token` function will return an error message.

