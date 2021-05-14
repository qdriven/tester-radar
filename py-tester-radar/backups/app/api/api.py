from fastapi import APIRouter

from .endpoints import utils, github

api_router = APIRouter()
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(github.router, prefix="/github", tags=["github"])