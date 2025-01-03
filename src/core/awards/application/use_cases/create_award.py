import uuid
from dataclasses import dataclass

from src.core.awards.domain.entities.award import Award
from src.core.awards.domain.entities.award_repository import AwardRepository


@dataclass(slots=True)
class CreateAward:
    
    respository: AwardRepository
    
    def execute(self, year: int, movie_id: uuid.UUID, winner: bool) -> Award:
        award = Award(year=year, movie=movie_id, winner=winner)
        self.respository.save(award)
        return award
