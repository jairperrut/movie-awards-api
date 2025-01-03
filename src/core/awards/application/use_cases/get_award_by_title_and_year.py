from dataclasses import dataclass

from src.core.awards.domain.entities.award import Award
from src.core.awards.domain.entities.award_repository import AwardRepository


@dataclass(slots=True)
class GetAwardByTitleAndYear:
    award_repository: AwardRepository

    def execute(self, title: str, year: int) -> Award:
        return self.award_repository.get_by_title_and_year(title, year)
