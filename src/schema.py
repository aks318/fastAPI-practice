from pydantic import BaseModel

class conversationCreate(BaseModel):
    title: str

class messageCreate(BaseModel):
    conversation_id: int
    user_role: str
    context: str