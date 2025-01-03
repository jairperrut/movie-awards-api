from abc import ABC, abstractmethod

from src.core.producers.domain.entities.producer import Producer


class ProducerRepository(ABC):


    @abstractmethod
    def get_by_name(self, name: str) -> Producer:
        pass

    @abstractmethod
    def save(self, producer: Producer) -> None:
        pass
