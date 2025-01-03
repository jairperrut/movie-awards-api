import uuid
from dataclasses import dataclass, field


@dataclass(slots=True)
class Producer:
    name: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Producer):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
