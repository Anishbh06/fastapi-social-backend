from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import URL

from app.core.config import settings


connection_url = URL.create(
    "mssql+pyodbc",
    username=settings.db_username,
    password=settings.db_password,
    host=settings.db_server,
    database=settings.db_name,
    query={
        "driver": settings.db_driver,
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
