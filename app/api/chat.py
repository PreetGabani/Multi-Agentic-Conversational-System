from fastapi import APIRouter, Body
from app.llm.openai_wrapper import get_llm_response
from app.rag.retriever import get_context_from_docs
from app.crm.db import save_chat_message, get_user_by_id
import uuid

router = APIRouter()

@router.post("/chat")
async def chat(user_id: str = Body(...), message: str = Body(...)):
    context = get_context_from_docs(message)
    response = get_llm_response(message, context)

    save_chat_message(user_id, message, response)
    return {
        "user_id": user_id,
        "input": message,
        "context_used": context,
        "response": response
    }
