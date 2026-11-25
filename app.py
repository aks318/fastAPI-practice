from contextlib import asynccontextmanager
from fastapi import FastAPI
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver

from AI import getWorkflow
from router import router

DB_URI = "postgresql://aakash:Aakash%40123@localhost:5432/chatbot"

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with AsyncPostgresSaver.from_conn_string(DB_URI) as checkpointer:
        await checkpointer.setup()

        app.state.workflow = getWorkflow(checkpointer)

        yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)