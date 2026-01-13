from fastapi import FastAPI
from app.database.database import engine


app = FastAPI(title="Social Media Backend")

@app.get("/")
def root():
    return {"status":"ok"}

@app.get("/db-check")
def db_check():
    with engine.connect() as conn:
        return {"db": "connected"}