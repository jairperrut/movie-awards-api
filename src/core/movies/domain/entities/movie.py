import uuid
from typing import Set
from dataclasses import dataclass, field

from src.core.producers.domain.entities.producer import Producer
from src.core.studio.domain.entities.studio import Studio


@dataclass(slots=True)
class Movie:
    title: str
    id: uuid.UUID = field(default_factory= uuid.uuid4)
    studios: Set[uuid.UUID | Studio] = field(default_factory=set)
    producers: Set[uuid.UUID | Producer] = field(default_factory=set)
