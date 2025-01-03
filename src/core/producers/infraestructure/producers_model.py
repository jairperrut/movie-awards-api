import uuid

from sqlmodel import Field, Relationship, SQLModel

from src.core.movies.infraestructure.movie_producer_model import MovieProducerLink


class ProducerModel(SQLModel, table=True):
    __tablename__ = "producers"

    id: uuid.UUID = Field(primary_key=True)
    name: str = Field(index=True, nullable=False)

    movies: list["MovieModel"] = Relationship(back_populates="producers", link_model=MovieProducerLink)
