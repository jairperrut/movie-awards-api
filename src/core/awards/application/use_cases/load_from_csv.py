import csv
import logging
from dataclasses import dataclass

from src.core.awards.application.use_cases.create_award import CreateAward
from src.core.awards.application.use_cases.get_award_by_title_and_year import GetAwardByTitleAndYear
from src.core.awards.domain.entities.award_repository import AwardRepository
from src.core.movies.application.use_cases.create_movie import CreateMovie
from src.core.movies.application.use_cases.get_movie import GetMovie
from src.core.movies.domain.entities.movie_repository import MovieRepository
from src.core.producers.application.use_cases.get_or_create_producer import GetOrCreateProducer
from src.core.producers.domain.entities.producer_repository import ProducerRepository
from src.core.studio.application.use_cases.get_or_create_studio import GetOrCreateStudio
from src.core.studio.domain.entities.studio_repository import StudioRepository

logger = logging.getLogger(__name__)

@dataclass(slots=True)
class LoadFromCSV:

    producer_repository: ProducerRepository
    studio_repository: StudioRepository
    movie_repository: MovieRepository
    award_repository: AwardRepository
        
    def execute(self, file_path: str) -> None:
        try:
            with open(file_path) as file:
                logger.info("Loading movies from CSV...")
                data = csv.DictReader(file, delimiter=';')
                for row in data:
                    award = GetAwardByTitleAndYear(self.award_repository).execute(row['title'], row["year"])
                    if not award:
                        movie = GetMovie(self.movie_repository).execute(row['title'])
                        if not movie:
                            producers = self.__extract_values(GetOrCreateProducer(self.producer_repository), row['producers'])
                            studios = self.__extract_values(GetOrCreateStudio(self.studio_repository), row['studios'])
                            movie = CreateMovie(self.movie_repository).execute(row["title"], producers, studios)

                        winner = row['winner'] == 'yes'
                        logger.info(f"Creating award for movie {movie.title}")
                        CreateAward(self.award_repository).execute(int(row["year"]), movie.id, winner)
            logger.info("Finished loading movies")
        except Exception:
            logger.exception("Error on loading movies")
    
    def __extract_values(self, use_case, value) -> set:
        return {use_case.execute(name).id for name in value.replace(' and ', ', ').split(', ')}
