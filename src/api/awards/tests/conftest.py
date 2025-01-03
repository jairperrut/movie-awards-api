import uuid
import pytest

from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm.session import Session
from sqlmodel import SQLModel

from src.api.main import create_app
from src.core.producers.infraestructure.producers_model import ProducerModel
from src.core.shared.infraestructure.db.engine import get_session
from src.core.studio.infraestructure.studio_model import StudioModel


@pytest.fixture()
def db_session():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    SQLModel.metadata.create_all(bind=engine)
    with Session(engine) as session:
        yield session

@pytest.fixture()
def override_get_session(db_session: Session):
    def _override_get_session():
        yield db_session

    return _override_get_session

@pytest.fixture()
def app(override_get_session) -> FastAPI:
    app = create_app()
    app.dependency_overrides[get_session] = override_get_session
    return app

@pytest.fixture()
def client_app(app: FastAPI) -> TestClient:
    return TestClient(app=app)

@pytest.fixture()
def mocked_producers(db_session: Session) -> list[ProducerModel]:
    producers = [
        ProducerModel(id=uuid.uuid4(), name="Producer A"),
        ProducerModel(id=uuid.uuid4(), name="Producer B"),
        ProducerModel(id=uuid.uuid4(), name="Producer C")
    ]
    db_session.add_all(producers)
    db_session.commit()
    return producers

@pytest.fixture()
def mocked_studios(db_session: Session) -> list[StudioModel]:
    studios = [
        StudioModel(id=uuid.uuid4(), name="Studio A"),
        StudioModel(id=uuid.uuid4(), name="Studio B"),
        StudioModel(id=uuid.uuid4(), name="Studio C")
    ]
    db_session.add_all(studios)
    db_session.commit()
    return studios
