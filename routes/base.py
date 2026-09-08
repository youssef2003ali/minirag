from fastapi import FastAPI, APIRouter 
import os


router = APIRouter(
    prefix="/api/v1",
    tags=["APIV1"]
)

@router.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {
        "app_name": app_name,
        "app_version": app_version,
        "message" : "WELCOME IAM WORKING FROM BASE ROUTE"
    }
