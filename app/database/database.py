from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import URL
from app.core.config import (DB_SERVER,DB_NAME,DB_USERNAME,DB_PASSWORD,DB_DRIVER,)

connection_url = URL.create(
    "mssql+pyodbc",
    username=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_SERVER,
    database=DB_NAME,
    query={
        "driver": DB_DRIVER,
        "TrustServerCertificate": "yes",
    },
)

engine = create_engine(
    connection_url,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()