from fastapi import FastAPI, APIRouter , Depends 
import os
from helpers.config import get_settings , Settings

router = APIRouter(
    prefix="/api/v1",
    tags=["APIV1"]
)

@router.get("/")
async def welcome(app_config : Settings = Depends(get_settings)):
    # app_config = get_settings()
    # app_name = os.getenv("APP_NAME")
    # app_version = os.getenv("APP_VERSION")
    app_name = app_config.APP_NAME
    app_version = app_config.APP_VERSION
    return {
        "app_name": app_name,
        "app_version": app_version,
        "message" : "WELCOME IAM WORKING FROM BASE ROUTE"
    }
