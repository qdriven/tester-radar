#!/usr/bin/env python
# -*- coding: utf-8 -*-

from clients import github_client
from app.github.schemas import gh_schemas

client = github_client.make_client()


def get_github_repo_info(repo_path: str) -> gh_schemas.RadarGithubRepo:
    repo = client.get_repo(repo_path)
    radar_gh_repo = gh_schemas.RadarGithubRepo.from_gh_repo(repo)
    return radar_gh_repo
