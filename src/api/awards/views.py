from fastapi import APIRouter, Depends

from src.core.awards.application.use_cases.get_winners_interval import GetWinnersInterval
from src.core.awards.infraestructure.orm_awards_repository import ORMAwardRepository
from src.core.shared.infraestructure.db.engine import get_session

router = APIRouter(prefix="/awards")

@router.get("/interval")
def find_interval(session=Depends(get_session)) -> GetWinnersInterval.Output:
    use_case = GetWinnersInterval(repository=ORMAwardRepository(session))
    result = use_case.execute()
    return result
