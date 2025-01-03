import uuid
from dataclasses import dataclass
from typing import Set

from src.core.movies.domain.entities.movie import Movie
from src.core.movies.domain.entities.movie_repository import MovieRepository


@dataclass(slots=True)
class CreateMovie:

    repositry: MovieRepository

    def execute(self, title: str, producers: Set[uuid.UUID], studios: Set[uuid.UUID]) -> Movie:
        movie = Movie(title=title, producers=producers, studios=studios)
        self.repositry.save(movie)
        return movie
