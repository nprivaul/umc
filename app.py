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
  
@app.get("/")
def home():
    return {"status": "backend alive"}

from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def answer_question(q):
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful academic assistant."},
            {"role": "user", "content": q}
        ]
    )
    return resp.choices[0].message.content
