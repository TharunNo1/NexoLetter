from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

is_sqlite = settings.db.DATABASE_URL.startswith("sqlite")
connect_args = {"check_same_thread": False} if is_sqlite else {}

engine = create_engine(
    settings.db.DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True,
    echo=settings.db.ECHO
    # pool_size=5,
    # max_overflow=10
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine,
)

Base = declarative_base()