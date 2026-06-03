from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    question: str

def answer_question(q):
    return f"You asked: {q} (backend not connected yet)"

@app.post("/api/chat")
def chat(query: Query):
    return {"answer": answer_question(query.question)}
  
