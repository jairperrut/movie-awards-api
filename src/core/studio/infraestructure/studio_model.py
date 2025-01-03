import uuid

from sqlmodel import Field, Relationship, SQLModel

from src.core.movies.infraestructure.movie_studio_model import MovieStudioLink


class StudioModel(SQLModel, table=True):
    __tablename__ = "studios"

    id: uuid.UUID = Field(primary_key=True)
    name: str = Field(index=True, nullable=False)

    movies: list["MovieModel"] = Relationship(back_populates="studios", link_model=MovieStudioLink)
