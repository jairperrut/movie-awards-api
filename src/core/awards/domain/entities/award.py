import uuid
from dataclasses import dataclass, field

from src.core.movies.domain.entities.movie import Movie


@dataclass(slots=True)
class Award:
    year: int
    movie: uuid.UUID | Movie
    winner: bool
    id: uuid.UUID = field(default_factory=uuid.uuid4)

@dataclass(slots=True)
class AwardFull:
    year: int
    movie: Movie
    winner: bool
    id: uuid.UUID = field(default_factory=uuid.uuid4)
