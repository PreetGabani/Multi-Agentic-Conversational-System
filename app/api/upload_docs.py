from fastapi import APIRouter, UploadFile, File
import os
import shutil

router = APIRouter()
UPLOAD_DIR = "uploads"

@router.post("/upload_docs")
async def upload_docs(file: UploadFile = File(...)):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "status": "uploaded"}

@router.post("/upload_docs")
async def upload_docs(file: UploadFile = File(...)):
    print(f"[DEBUG] Received file: {file.filename}")  # DEBUG
    ...
