import uuid
from sqlmodel import Field, SQLModel


class MovieStudioLink(SQLModel, table=True):

    movie_id: uuid.UUID = Field(foreign_key="movies.id", primary_key=True)
    studio_id: uuid.UUID = Field(foreign_key="studios.id", primary_key=True)
