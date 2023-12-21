"""The main file for a FastAPI application"""
from fastapi import FastAPI


app = FastAPI(
    title="FastAPI Auth0 Test",
    description="A simple fastapi backend with Auth0 authentication",
    version="0.1.0"
)


@app.get("/")
async def root():
    """The root endpoint for the API

    Returns:
        dict: A dict with a simple message
    """
    return {"message": "Hello World"}
