from fastapi import FastAPI
from app.database.database import engine, Base
from app.routers import user, auth, post
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



Base.metadata.create_all(bind=engine)

app = FastAPI(title="Social Media Backend")


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(user.router)
app.include_router(auth.router)
app.include_router(post.router)


 