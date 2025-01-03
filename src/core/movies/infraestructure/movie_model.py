import uuid

from sqlmodel import Field, Relationship, SQLModel

from src.core.movies.infraestructure.movie_producer_model import MovieProducerLink
from src.core.movies.infraestructure.movie_studio_model import MovieStudioLink


class MovieModel(SQLModel, table=True):
    __tablename__ = "movies"

    id: uuid.UUID = Field(primary_key=True)
    title: str
    studios: list["StudioModel"] = Relationship(back_populates="movies", link_model=MovieStudioLink)
    producers: list["ProducerModel"] = Relationship(back_populates="movies", link_model=MovieProducerLink)
