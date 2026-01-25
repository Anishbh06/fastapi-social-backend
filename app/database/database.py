# app/database/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import URL

from app.core.config import settings

# Pull port from settings if present (fall back to 1433)
try:
    db_port = int(settings.db_port) if getattr(settings, "db_port", None) else 1433
except Exception:
    db_port = 1433

connection_url = URL.create(
    "mssql+pyodbc",
    username=settings.db_username,
    password=settings.db_password,
    host=settings.db_server,
    port=db_port,
    database=settings.db_name,
    query={
        "driver": settings.db_driver,
        # container -> host SSL / certs messy; easier to accept trust on dev
        "TrustServerCertificate": "yes",
    },
)

# Use pool_pre_ping to avoid stale connections
engine = create_engine(connection_url, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
