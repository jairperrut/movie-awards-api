from typing import Any, Generator

from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

from src.settings import settings

engine = create_engine(
    "sqlite:///movie.db",
    connect_args={"check_same_thread": False},
    echo=settings.db_echo
)

def create_db() -> None:
    SQLModel.metadata.drop_all(bind=engine)
    SQLModel.metadata.create_all(bind=engine)

def get_session() -> Generator[Session, Any, None]:
    with Session(engine) as session:
        yield session
