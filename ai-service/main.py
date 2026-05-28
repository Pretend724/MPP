from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI

app = FastAPI()

class Query(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "AI Service is running"}

@app.post("/chat")
async def chat(query: Query):
    # This is a placeholder for LangChain logic
    return {"response": f"You said: {query.text}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
