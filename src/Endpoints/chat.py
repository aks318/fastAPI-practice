from fastapi import APIRouter, Depends, status, HTTPException, Request
from langchain.messages import AIMessage, HumanMessage
from sqlalchemy.orm import Session
from database import engine, get_db
from model import Base, conversation, message
from schema import messageCreate
router = APIRouter()

# Create Table
Base.metadata.create_all(bind = engine)


@router.get("/getNewChat")
async def newChat(db: Session = Depends(get_db)):
    new_convo = conversation(title="new chat")

    db.add(new_convo)
    db.commit()
    db.refresh(new_convo)

    return new_convo

    

@router.get("/loadChat/{id}")
async def loadChat(id, db: Session = Depends(get_db)):
    load_chat = db.get(conversation, id)
    if not load_chat:
        raise HTTPException(
            status_code=404,
            detail="Conversion not found"
        )
    return load_chat

@router.get('/loadAllChat')
async def loadAllChat(db: Session = Depends(get_db)):
    load_all_chat = db.query(conversation).all()
    return load_all_chat


@router.post("/sendchat")
async def sendchat(req: messageCreate, request: Request, db: Session = Depends(get_db)):
    # history = db.query(message).filter(
    #     message.conversation_id == req.conversation_id
    # ).order_by(message.id.asc()).all()

    # messageArr = []

    # for msg in history:
    #     if msg.user_role == "user":
    #         messageArr.append(HumanMessage(content=msg.context))
    #     elif msg.user_role == "assistant":
    #         messageArr.append(AIMessage(content=msg.context))

    # messageArr.append(HumanMessage(content=req.context))

    result = await request.app.state.workflow.ainvoke(
    {
        "messages": [
            HumanMessage(content=req.context)
        ]
    },
    config={
        "configurable": {
            "thread_id": str(req.conversation_id)
        }
    }
)

    ai_response = result["messages"][-1].content

    print(ai_response)

    db.add(message(
        conversation_id= req.conversation_id,
        user_role= "user",
        context= req.context
    ))

    db.add(message(
        conversation_id= req.conversation_id,
        user_role= "assistant",
        context= ai_response
    ))

    db.commit()
    return ai_response