from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.core.producers.domain.entities.producer import Producer
from src.core.producers.domain.entities.producer_repository import ProducerRepository
from src.core.producers.infraestructure.producers_model import ProducerModel

@dataclass(slots=True)
class ORMProducerRepository(ProducerRepository):

    session: Session

    def get_by_name(self, name: str) -> Producer | None:
        result = self.session.execute(select(ProducerModel).filter(ProducerModel.name == name)).scalar()
        if result:
            return Producer(
                id=result.id,
                name=result.name
            )

    def save(self, producer: Producer) -> None:
        self.session.add(ProducerModel(
            id=producer.id,
            name=producer.name
        ))
        self.session.commit()
