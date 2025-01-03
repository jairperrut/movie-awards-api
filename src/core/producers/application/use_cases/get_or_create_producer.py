from dataclasses import dataclass

from src.core.producers.domain.entities.producer import Producer
from src.core.producers.domain.entities.producer_repository import ProducerRepository


@dataclass(slots=True)
class GetOrCreateProducer:

    repository: ProducerRepository

    def execute(self, name: str) -> Producer:
        producer = self.repository.get_by_name(name)
        if not producer:
            producer = Producer(name=name)
            self.repository.save(producer)
        return producer
