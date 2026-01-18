from fastapi import FastAPI
from app.database.database import engine, Base
from app.routers import user, auth


Base.metadata.create_all(bind=engine)


app = FastAPI(title="Social Media Backend")

# @app.get("/")
# def root():
#     return {"status":"ok"}

# @app.get("/db-check")
# def db_check():
#     with engine.connect() as conn:
#         return {"db": "connected"}

app.include_router(user.router)
app.include_router(auth.router)

 