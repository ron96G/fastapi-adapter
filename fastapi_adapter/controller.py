from typing import Union

import magic
from fastapi import UploadFile
from fastapi.exceptions import HTTPException

from .models import *
from .routes import APIResponse, Controller, FileResponse, MessageRequest


class WhatsAppController(Controller):

    mime = magic.Magic(mime=True)

    async def get_download_media(self, media_id) -> Union[FileResponse, APIResponse]:
        def iterfile():
            with open(media_id, mode="rb") as file_like:
                yield from file_like

        try:
            return FileResponse(iterfile(), media_type=self.mime.from_file(media_id))

        except OSError as e:
            raise HTTPException(status_code=404, detail=e.strerror)

    async def post_send_message(self, body: MessageRequest) -> Union[None, APIResponse]:
        return {
            "status": Status.success,
            "reason": f"Sending message with type {body.type}",
        }

    async def post_upload_media(self, file: UploadFile) -> Union[None, APIResponse]:
        try:
            with open(f"./{file.filename}", "wb") as out_file:
                content = await file.read()
                out_file.write(content)
        except OSError as e:
            return {"status": Status.failed, "reason": str(e)}

        return {"status": Status.success, "reason": f"saving file {file.filename}"}
