from typing import Any

from fastapi import APIRouter

from backups.app.schemas import github
from backups.app.schemas import GithubRepoQuery
from backups.feeds.collectors import make_client

router = APIRouter()


@router.post("/github", response_model=github)
def get_repo_starts(request_in: GithubRepoQuery) -> Any:
    github_client = make_client()
    repo = github_client.get_repo(request_in.repo_url)
    return repo
