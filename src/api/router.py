from fastapi import APIRouter

from src.api.awards.views import router as awards_router


router = APIRouter(prefix="/api")

router.include_router(router=awards_router, tags=["Awards"])
