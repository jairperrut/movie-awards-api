from dataclasses import dataclass

from src.core.studio.domain.entities.studio import Studio
from src.core.studio.domain.entities.studio_repository import StudioRepository


@dataclass(slots=True)
class GetOrCreateStudio:

    repository: StudioRepository

    def execute(self, name: str) -> Studio:
        studio = self.repository.get_by_name(name)
        if not studio:
            studio = Studio(name=name)
            self.repository.save(studio)
        return studio
