from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.core.movies.domain.entities.movie import Movie
from src.core.movies.domain.entities.movie_repository import MovieRepository
from src.core.movies.infraestructure.movie_model import MovieModel
from src.core.movies.infraestructure.movie_producer_model import MovieProducerLink
from src.core.movies.infraestructure.movie_studio_model import MovieStudioLink

@dataclass(slots=True)
class ORMMovieRepository(MovieRepository):

    session: Session

    def get_by_title(self, title: str) -> Movie | None:
        result = self.session.execute(select(MovieModel).filter(MovieModel.title == title)).scalar()
        if result:
            return Movie(
                id=result.id,
                title=result.title,
                studios={studio.id for studio in result.studios},
                producers={producer.id for producer in result.producers}
            )

    def save(self, movie: Movie) -> None:
        for producer in movie.producers:
            self.session.add(MovieProducerLink(movie_id=movie.id, producer_id=producer))
        for studio in movie.studios:
            self.session.add(MovieStudioLink(movie_id=movie.id, studio_id=studio))
        self.session.add(MovieModel(
            id=movie.id,
            title=movie.title
        ))
        self.session.commit()
