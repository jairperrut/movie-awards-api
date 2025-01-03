import uuid
from sqlmodel import Field, Relationship, SQLModel


class AwardModel(SQLModel, table=True):
    __tablename__ = "awards"

    id: uuid.UUID = Field(primary_key=True)
    movie_id: uuid.UUID = Field(foreign_key="movies.id", nullable=False)
    year: int
    winner: bool

    movie: "MovieModel" = Relationship()
