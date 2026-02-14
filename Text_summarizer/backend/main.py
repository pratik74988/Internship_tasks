from fastapi import FastAPI
from pydantic import BaseModel
from summarizer import generate_summary

app = FastAPI()

class Article (BaseModel):
    text : str


@app.post("/summarize")
def summarize (article:Article):
    summary = generate_summary(article.text)
    return {"summary": summary}