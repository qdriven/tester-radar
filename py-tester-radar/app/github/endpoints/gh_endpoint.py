from fastapi import APIRouter

from app.github.schemas.gh_schemas import RadarGithubRepo
from app.github.service import gh_service

router = APIRouter()


@router.get("/github", response_model=RadarGithubRepo)
def get_github_repo_status(repo_name: str):
    return gh_service.get_github_repo_info(repo_name)