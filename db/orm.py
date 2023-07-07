from __future__ import annotations
import os
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy.pool import QueuePool
from core.configuration import settings
from tools.exceptions.db import DBConnectionException

Base = declarative_base()


def get_db_engine() -> Engine:
    try:
        engine = create_engine(
            f"{settings.DB_DRIVER}:///{os.path.join(settings.BASE_DIR, 'db', f'{settings.DB_NAME}.db')}",
            # For async postgres
            # f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
            # More detailed logging is mentioned here
            # https://stackoverflow.com/questions/48812971/flask-sqlalchemy-advanced-logging
            echo=settings.LOG_ORM,
            pool_size=100,
            max_overflow=0,
            poolclass=QueuePool,
        )
        return engine
    except Exception as e:
        raise DBConnectionException(f"Database connection failed. Error message: {e}")
        # logger.exception(f"Database connection failed. Error message: {e}")


def create_sync_session(*args, **kwargs) -> sessionmaker:
    return sessionmaker(*args, **kwargs)


try:
    SyncSession = create_sync_session(bind=get_db_engine(), expire_on_commit=False, autocommit=False, class_=Session)
except Exception:
    raise
