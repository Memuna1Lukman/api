from fastapi import FastAPI
from sqlalchemy.orm import Session
import psycopg2
from . import models
from .router import user



app = FastAPI()



app.include_router(user.router)

