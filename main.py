from fastapi import FastAPI, APIRouter 
from dotenv import load_dotenv
load_dotenv(".env")

from routes import base

app = FastAPI()
app.include_router(base.router)
