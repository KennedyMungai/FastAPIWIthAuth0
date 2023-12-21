"""FastAPI starter sample
"""

from fastapi import FastAPI, Depends, Response, status
from fastapi.security import HTTPBearer

app = FastAPI()
token_auth_scheme = HTTPBearer()


@app.get("/api/public")
def public():
    """No access token required to access this route"""

    result = {
        "status": "success",
        "msg": ("Hello from a public endpoint! "
                "You don't need to be authenticated to see this.")
    }
    return result


@app.get("/api/private")
def private(_token: str = Depends(token_auth_scheme)):
    """A valid access token is required to access this route"""

    # We need to protect this endpoint!

    result = {
        "status": "success",
        "msg": ("Hello from a private endpoint! "
                "You need to be authenticated to see this.")
    }
    return result
