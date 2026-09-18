from fastapi import FastAPI, APIRouter , Depends , UploadFile ,status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings , Settings
from controllers import ProjectController, DataController
import aiofiles
from models import ResponseSignal
import logging

logger = logging.getLogger("uvicorn.error")

data_router = APIRouter(
    prefix = "/api/v1/data",
    tags =["V1","Data"]
    )

@data_router.post("/upload/{project_id}")
async def upload_data(file : UploadFile , project_id : str, app_config : Settings = Depends(get_settings)
                      ):

    data_controller = DataController()
    is_valid , signal = data_controller.validate_upload_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {
                "signal" : signal
            }
        )

    project_path = ProjectController().get_project_path(project_id=project_id)
    file_path , file_id = data_controller.genereate_unique_filepath(
        orig_file_name = file.filename,
        project_id = project_id
    )
    try :

        async with aiofiles.open(file_path,"wb") as f:
            while chunck := await  file.read(app_config.FILE_CHUNK_SIZE):
                await f.write(chunck)
    except Exception as e:
        logger.error(f"while uploading file {file.filename} for project {project_id} : {str(e)}")
        return JSONResponse(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            content = {
                "signal" : ResponseSignal.FILE_UPLOAD_FAILED.value
                # "error" : str(e)
            }
        )

    return JSONResponse(
        content = {
            "signal" : ResponseSignal.FILE_UPLOAD_SUCCESS.value,
            "file_id": file_id
        }
    )




