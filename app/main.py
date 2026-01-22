from fastapi import FastAPI
from app.database.database import engine, Base
from app.routers import user, auth, post


Base.metadata.create_all(bind=engine)


app = FastAPI(title="Social Media Backend")

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(post.router)


 