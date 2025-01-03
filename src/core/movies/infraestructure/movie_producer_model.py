import uuid

from sqlmodel import Field, SQLModel


class MovieProducerLink(SQLModel, table=True):

    movie_id: uuid.UUID = Field(foreign_key="movies.id", primary_key=True)
    producer_id: uuid.UUID = Field(foreign_key="producers.id", primary_key=True)
