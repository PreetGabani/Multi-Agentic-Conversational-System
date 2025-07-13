from fastapi import FastAPI, UploadFile, File
import shutil
import os
from pydantic import BaseModel
from app.crm.db import save_conversation

from app.api import reset


from app.api import crm

app = FastAPI()
app.include_router(reset.router)

UPLOAD_DIR = "uploads"

@app.on_event("startup")
def startup_event():
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

app.include_router(crm.router)

@app.post("/upload_docs")
async def upload_docs(file: UploadFile = File(...)):
    print(f"Received file: {file.filename}")
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "status": "uploaded"}

class ChatRequest(BaseModel):
    user_id: str
    message: str


@app.post("/chat")
def chat(req: ChatRequest):
    user_id = req.user_id
    user_message = req.message

    response_text = "A deal usually takes 30-60 days. Let me know if you want details on any other topics."

    save_conversation(user_id, user_message, response_text)

    return {"response": response_text}