#!/usr/bin/env python
# -*- coding: utf-8 -*-
from github.Repository import Repository

from collectors.github.base import RadarRepo
from collectors.github.client import make_default_gh_client_by_access_token


def test_from_gh_repo():
    gh = make_default_gh_client_by_access_token()
    repo = RadarRepo.from_gh_repo(gh.get_user().get_repo("qdriven"))
    assert repo.name == 'qdriven/qdriven'
    result = repo.to_json()
    print(result)