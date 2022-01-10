# generated by fastapi-codegen. DO NOT EDIT.
#   filename:  openapi.yaml
#   timestamp: 2022-01-10T20:57:37+00:00

from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .routes import *

from .controller import WhatsAppController

common_responses = {
    501: {"description": "The requested controller has not been implemented"}
}

app = FastAPI(
    title="openapi",
    version="1.0",
    description="An abstract API that can be used to send messages.",
    contact={"name": "FooBar"},
    servers=[{"url": "http://localhost:8000", "description": "Localhost"}],
    responses={**common_responses},
)


@app.exception_handler(NotImplementedException)
async def not_implemented_exception_handler(
    request: Request, exc: NotImplementedException
):
    return JSONResponse(
        status_code=501,
        content={"message": "The requested controller has not been implemented"},
    )


@app.exception_handler(HTTPException)
async def default_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


controller = WhatsAppController()

configure_routes__downloadMedia_media_id(app, controller)
configure_routes__sendMessage(app, controller)
configure_routes__uploadMedia(app, controller)
