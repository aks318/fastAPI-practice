

from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic import BaseModel

from router import router

app = FastAPI()

app.include_router(router)