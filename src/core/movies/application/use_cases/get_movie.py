from dataclasses import dataclass

from src.core.movies.domain.entities.movie import Movie
from src.core.movies.domain.entities.movie_repository import MovieRepository


@dataclass(slots=True)
class GetMovie:

    repository: MovieRepository

    def execute(self, title: str) -> Movie:
        return self.repository.get_by_title(title)
