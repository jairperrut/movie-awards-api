from dataclasses import dataclass
from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.core.awards.domain.entities.award import Award
from src.core.awards.domain.entities.award_repository import AwardRepository
from src.core.awards.infraestructure.award_model import AwardModel
from src.core.movies.domain.entities.movie import Movie
from src.core.movies.infraestructure.movie_model import MovieModel
from src.core.producers.domain.entities.producer import Producer
from src.core.studio.domain.entities.studio import Studio


@dataclass(slots=True)
class ORMAwardRepository(AwardRepository):

    session: Session

    def save(self, award: Award) -> None:
        db_data = AwardModel(
            id=award.id,
            movie_id=award.movie,
            year=award.year,
            winner=award.winner
        )
        self.session.add(db_data)
        self.session.commit()

    def get_by_title_and_year(self, title, year) -> Award | None:
        select_stmt = select(AwardModel).join(MovieModel).filter(MovieModel.title == title, AwardModel.year == year)
        result = self.session.execute(select_stmt).scalar()
        if result:
            return Award(
                id=result.id,
                year=result.year,
                movie=result.movie_id,
                winner=result.winner
            )

    def get_winners(self) -> List[Award]:
        awards = self.session.execute(select(AwardModel).filter(AwardModel.winner.is_(True))).scalars().all()
        return [
            Award(
                id=award.id,
                year=award.year,
                movie=Movie(
                    id=award.movie_id,
                    title=award.movie.title,
                    studios={Studio(
                        id=studio.id,
                        name=studio.name,
                        ) for studio in award.movie.studios
                    },
                    producers={Producer(
                        id=producer.id,
                        name=producer.name,
                        ) for producer in award.movie.producers
                    }
                ),
                winner=award.winner
            )
            for award in awards
        ]
