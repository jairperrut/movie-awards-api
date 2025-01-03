from abc import ABC, abstractmethod

from src.core.studio.domain.entities.studio import Studio


class StudioRepository(ABC):


    @abstractmethod
    def get_by_name(self, name: str) -> Studio:
        pass

    @abstractmethod
    def save(self, producer: Studio) -> None:
        pass
