from fastapi import APIRouter, Body
from app.crm.db import create_user, update_user, get_conversations
from pydantic import BaseModel
from typing import Dict

class UpdateUserRequest(BaseModel):
    user_id: str
    user: Dict

router = APIRouter()

@router.post("/crm/create_user")
def create(user: dict = Body(...)):
    return create_user(user)

@router.put("/crm/update_user")
def update(req: UpdateUserRequest):
    return update_user(req.user_id, req.user)


@router.get("/crm/conversations/{user_id}")
def get_convos(user_id: str):
    return get_conversations(user_id)
