
from fastapi import FastAPI

from app.schemas.gh_schemas import RadarGithubRepo
from app.service import gh_service

app = FastAPI()


@app.get("/github", response_model=RadarGithubRepo)
def get_github_repo_status(repo_name: str):
    return gh_service.get_github_repo_info(repo_name)
