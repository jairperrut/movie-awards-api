from abc import ABC, abstractmethod
from typing import List

from src.core.awards.domain.entities.award import Award
from src.core.awards.infraestructure.award_model import AwardModel


class AwardRepository(ABC):
    
    @abstractmethod
    def save(self, award: Award):
        pass
    
    @abstractmethod
    def get_by_title_and_year(self, title, year):
        pass

    @abstractmethod
    def get_winners(self) -> List[AwardModel]:
        pass
