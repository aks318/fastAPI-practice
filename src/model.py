from sqlalchemy import Column, ForeignKey, Integer, String

from database import Base

class conversation(Base):

    __tablename__ = "conversation"

    id = Column(Integer, primary_key=True)
    title = Column(String)

class message(Base):
    __tablename__= "message"
    id = Column(Integer, primary_key=True)
    conversation_id = Column(Integer, ForeignKey("conversation.id"), nullable=False)
    user_role = Column(String, default="user")
    context = Column(String)