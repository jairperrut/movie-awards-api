from abc import ABC, abstractmethod

from src.core.movies.domain.entities.movie import Movie


class MovieRepository(ABC):

    @abstractmethod
    def get_by_title(self, title: str) -> Movie:
        pass

    @abstractmethod
    def save(self, movie: Movie) -> None:
        pass
