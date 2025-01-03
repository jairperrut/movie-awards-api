import uuid

from fastapi.testclient import TestClient
from sqlalchemy.orm.session import Session

from src.core.awards.infraestructure.award_model import AwardModel
from src.core.movies.infraestructure.movie_model import MovieModel
from src.core.producers.infraestructure.producers_model import ProducerModel
from src.core.studio.infraestructure.studio_model import StudioModel

class TestGetIntervalMinMax:

    def test_no_awards(self, client_app: TestClient):
        response = client_app.get("/awards/interval")
        assert response.status_code == 200

        data = response.json()

        assert data.get("min") == []
        assert data.get("max") == []

    def test_one_award(self, db_session: Session, client_app: TestClient, mocked_producers: list[ProducerModel], mocked_studios: list[StudioModel]):
        award_a = AwardModel(
            id=uuid.uuid4(),
            movie=MovieModel(
                id=uuid.uuid4(),
                title="Movie A",
                producers = [mocked_producers[0], mocked_producers[1]],
                studios = [mocked_studios[0]],
            ),
            year=2015,
            winner=True
        )
        db_session.add(award_a)
        db_session.commit()

        response = client_app.get("/awards/interval")
        assert response.status_code == 200

        data = response.json()

        assert data.get("min") == []
        assert data.get("max") == []

    def test_award_winner_two_times(self, db_session: Session, client_app: TestClient, mocked_producers: list[ProducerModel], mocked_studios: list[StudioModel]):
        award_a = AwardModel(
            id=uuid.uuid4(),
            movie=MovieModel(
                id=uuid.uuid4(),
                title="Movie A",
                producers = [mocked_producers[0], mocked_producers[1]],
                studios = [mocked_studios[0]],
            ),
            year=2015,
            winner=True
        )
        award_b = AwardModel(
            id=uuid.uuid4(),
            movie=MovieModel(
                id=uuid.uuid4(),
                title="Movie B",
                producers = [mocked_producers[0]],
                studios = [mocked_studios[1]],
            ),
            year=2016,
            winner=True
        )
        db_session.add_all([award_a, award_b])
        db_session.commit()

        response = client_app.get("/awards/interval")
        assert response.status_code == 200

        data = response.json()

        assert data.get("min") == [{'producer': 'Producer A', 'interval': 1, 'previousWin': 2015, 'followingWin': 2016}]
        assert data.get("max") == [{'producer': 'Producer A', 'interval': 1, 'previousWin': 2015, 'followingWin': 2016}]

    def test_get_interval_multiple_winners(self, db_session: Session, client_app: TestClient, mocked_producers: list[ProducerModel], mocked_studios: list[StudioModel]):
        awards = [AwardModel(
            id=uuid.uuid4(),
            movie=MovieModel(
                id=uuid.uuid4(),
                title="Movie A",
                producers = [mocked_producers[0], mocked_producers[1]],
                studios = [mocked_studios[0]],
            ),
            year=2015,
            winner=True
        ),
        AwardModel(
            id=uuid.uuid4(),
            movie=MovieModel(
                id=uuid.uuid4(),
                title="Movie E",
                producers = [mocked_producers[0]],
                studios = [mocked_studios[0]],
            ),
            year=2016,
            winner=False
        ),
        AwardModel(
            id=uuid.uuid4(),
            movie=MovieModel(
                id=uuid.uuid4(),
                title="Movie B",
                producers = [mocked_producers[0]],
                studios = [mocked_studios[1]],
            ),
            year=2017,
            winner=True
        ),
        AwardModel(
            id=uuid.uuid4(),
            movie=MovieModel(
                id=uuid.uuid4(),
                title="Movie C",
                producers = [mocked_producers[1], mocked_producers[2]],
                studios = [mocked_studios[2]],
            ),
            year=2017,
            winner=True
        ),
        AwardModel(
            id=uuid.uuid4(),
            movie=MovieModel(
                id=uuid.uuid4(),
                title="Movie D",
                producers = [mocked_producers[2]],
                studios = [mocked_studios[0]],
            ),
            year=2020,
            winner=True
        )]
        db_session.add_all(awards)
        db_session.commit()
        response = client_app.get("/awards/interval")
        assert response.status_code == 200

        data = response.json()

        assert sorted(data.get("min"), key=lambda x: (x['producer'], x['interval'], x['previousWin'], x['followingWin'])) == sorted([
            {'producer': 'Producer A', 'interval': 2, 'previousWin': 2015, 'followingWin': 2017},
            {'producer': 'Producer B', 'interval': 2, 'previousWin': 2015, 'followingWin': 2017}
        ], key=lambda x: (x['producer'], x['interval'], x['previousWin'], x['followingWin']))

        assert data.get("max") == [{'producer': 'Producer C', 'interval': 3, 'previousWin': 2017, 'followingWin': 2020}]
