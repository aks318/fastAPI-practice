from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

class AuthResponse(BaseModel):
    email: str
    passs: str

router = APIRouter()



@router.post(
    "registration",
    response_model=AuthResponse,
    status_code=status.HTTP_201_CREATED
    )
def registration(req: AuthResponse):
    return req.model_dump()

