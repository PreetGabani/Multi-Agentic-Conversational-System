from fastapi import APIRouter

router = APIRouter()

@router.post("/reset")
def reset_chat():
    return {"status": "Reset implemented."}
