# Multi-Agentic Conversational AI System

1. Clone repo and install dependencies:
python -m venv venv
source venv\Scripts\activate ( for windows)
pip install fastapi uvicorn pymongo openai pandas python-dotenv

2. Add your API keys to .env:
OPENAI_API_KEY=your_key_here
MONGO_URI=mongodb://localhost:27017

3. Run the API:
uvicorn app.main:app --reload

## Endpoints

- POST `/chat`: Ask the assistant with user_id and message.
- POST `/upload_docs`: Upload CSV/JSON/PDF/TXT.
- POST `/crm/create_user`: Create user with details.
- PUT `/crm/update_user`: Update user.
- GET `/crm/conversations/{user_id}`: Get full chat history.
- POST `/reset`: reset.
