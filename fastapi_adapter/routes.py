# generated by fastapi-codegen. DO NOT EDIT.
#   filename:  openapi.yaml
#   timestamp: 2022-01-10T20:57:37+00:00

from __future__ import annotations

from typing import Any, Union

from fastapi import FastAPI, UploadFile
from fastapi.exceptions import HTTPException
from fastapi.param_functions import File
from starlette.responses import StreamingResponse

from .models import APIResponse, MessageRequest


class FileResponse(StreamingResponse):
    media_type = "*/*"


class NotImplementedException(Exception):
    pass


class Controller:
    async def get_download_media(self, media_id: Any) -> Union[bytes, APIResponse]:
        raise NotImplementedException()

    async def post_send_message(self, body: Any) -> Union[None, APIResponse]:
        raise NotImplementedException()

    async def post_upload_media(self, file: Any) -> APIResponse:
        raise NotImplementedException()


def configure_routes__downloadMedia_media_id(app: FastAPI, controller: Controller) -> None:
    @app.get(
        "/downloadMedia/{media_id}",
        response_model=bytes,
        response_model_exclude_none=True,
        response_class=FileResponse,
        tags=["media"],
        responses={
            "200": {"model": bytes, "description": "Media has been downloaded"},
            "404": {"model": APIResponse, "description": "Not Found"},
        },
    )
    async def get_download_media(media_id: str) -> Union[bytes, APIResponse]:
        """
        Download Media File
        This endpoint can be used to download media files.
        """

        return await controller.get_download_media(media_id)


def configure_routes__sendMessage(app: FastAPI, controller: Controller) -> None:
    @app.post(
        "/sendMessage",
        response_model=None,
        response_model_exclude_none=True,
        tags=["messaging"],
        responses={
            "202": {
                "model": APIResponse,
                "description": "The message request was accepted and will be processed by the system.",
            },
            "400": {
                "model": APIResponse,
                "description": "The request was rejected due to invalid input. See the response for reasons.",
            },
        },
    )
    async def post_send_message(
        body: MessageRequest = None,
    ) -> Union[None, APIResponse]:
        """
        Send Message
        Send a message via the defined channel
        """

        return await controller.post_send_message(body)


def configure_routes__uploadMedia(app: FastAPI, controller: Controller) -> None:
    @app.post(
        "/uploadMedia",
        response_model=APIResponse,
        response_model_exclude_none=True,
        tags=["media"],
        responses={"200": {"model": APIResponse, "description": "Upload successful"}},
    )
    async def post_upload_media(file: UploadFile = File(default=None)) -> APIResponse:
        """
        Upload Media File
        This endpoint can be used to upload media files.
        """

        return await controller.post_upload_media(file)