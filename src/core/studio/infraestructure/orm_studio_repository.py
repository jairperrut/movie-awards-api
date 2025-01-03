from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.core.studio.domain.entities.studio import Studio
from src.core.studio.domain.entities.studio_repository import StudioRepository
from src.core.studio.infraestructure.studio_model import StudioModel

@dataclass(slots=True)
class ORMStudioRepository(StudioRepository):

    session: Session

    def get_by_name(self, name: str) -> Studio | None:
        result = self.session.execute(select(StudioModel).filter(StudioModel.name == name)).scalar()
        if result:
            return Studio(
                id=result.id,
                name=result.name
            )

    def save(self, studio: Studio) -> None:
        self.session.add(StudioModel(
            id=studio.id,
            name=studio.name
        ))
        self.session.commit()
