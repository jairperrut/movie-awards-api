from dataclasses import dataclass


@dataclass(slots=True)
class Interval:
    producer: str
    interval: int
    previousWin: int
    followingWin: int
