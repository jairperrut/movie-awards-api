import logging
from logging.config import dictConfig
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core.awards.infraestructure.orm_awards_repository import ORMAwardRepository
from src.core.movies.infraestructure.orm_movie_repository import ORMMovieRepository
from src.core.producers.infraestructure.orm_producer_repository import ORMProducerRepository
from src.core.shared.infraestructure.db.engine import get_session
from src.core.awards.application.use_cases.load_from_csv import LoadFromCSV
from src.core.studio.infraestructure.orm_studio_repository import ORMStudioRepository
from src.settings import log_config
from src.core.shared.infraestructure.db.engine import create_db
from src.api.awards.views import router


logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Startup: Initializing resources")
    create_db()
    with next(get_session()) as session:
        LoadFromCSV(
            award_repository=ORMAwardRepository(session),
            movie_repository=ORMMovieRepository(session),
            producer_repository=ORMProducerRepository(session),
            studio_repository=ORMStudioRepository(session),
        ).execute('movielist.csv')
    yield
    logger.info("Shutdown: Releasing resources")

def create_app() -> FastAPI:
    dictConfig(log_config)

    app = FastAPI(
        title="Movie Awards API",
        description="FastAPI service for Movie Awards",
        version="0.0.1",
        lifespan=lifespan
    )

    app.include_router(router=router)

    return app
