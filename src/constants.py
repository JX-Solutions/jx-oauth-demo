import os

# Required Settings - OAuth
CLIENT_ID = os.getenv("CRM_CLIENT_ID")
CLIENT_SECRET = os.getenv("CRM_CLIENT_SECRET")
REDIRECT_URI = os.getenv("CRM_REDIRECT_URI")
AUTHORIZATION_URL = os.getenv("AUTHORIZATION_URL")
TOKEN_URL = os.getenv("TOKEN_URL")
SCOPES = os.getenv("CRM_SCOPES")

# Optional Settings - Token refresh testing
REFRESH_TOKEN = os.getenv("CRM_REFRESH_TOKENs")
