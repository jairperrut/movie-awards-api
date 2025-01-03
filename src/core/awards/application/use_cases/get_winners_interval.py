
from typing import List
from collections import defaultdict
from dataclasses import dataclass

from src.core.awards.domain.entities.award_repository import AwardRepository
from src.core.awards.domain.entities.interal import Interval


@dataclass(slots=True)
class GetWinnersInterval:

    repository: AwardRepository
    
    @dataclass(slots=True)
    class Output:
        min: List[Interval]
        max: List[Interval]
    
    def execute(self) -> "Output":
        awards = self.repository.get_winners()

        producer_wins = defaultdict(list)

        for award in awards:
            if award.winner:
                for producer in award.movie.producers:
                    producer_wins[producer.name].append(award.year)

        intervals = []

        for producer, years in producer_wins.items():
            if len(years) > 1:
                sorted_years = sorted(years)
                for i in range(len(sorted_years) - 1):
                    interval = sorted_years[i + 1] - sorted_years[i]
                    intervals.append(
                        Interval(
                            producer=producer,
                            interval=interval,
                            previousWin=sorted_years[i],
                            followingWin=sorted_years[i + 1]
                        )
                    )

        if intervals:
            min_interval = min(interval.interval for interval in intervals)
            max_interval = max(interval.interval for interval in intervals)

            min_producers = [
                interval for interval in intervals if interval.interval == min_interval
            ]
            max_producers = [
                interval for interval in intervals if interval.interval == max_interval
            ]

            return self.Output(min_producers, max_producers)
        else:
            return self.Output([], [])
