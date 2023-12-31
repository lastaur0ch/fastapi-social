from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Optional, List
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

# @app.get("/")
# def root():
#     return {"message": "API works"}