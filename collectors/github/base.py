#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   
#   Author  :  patrick 
#   Date    :  2020/2/16 
#   Desc    :  github models
import json
from dataclasses import dataclass

from dataclasses_json import dataclass_json
from github.Repository import Repository

from collectors.base import BaseCollector
from collectors.github.client import make_client


# @dataclass_json
@dataclass
class RadarRepo:
    name: str
    url: str
    stars: int
    topics: [str]
    desc: str
    forks: int
    languages: []

    @staticmethod
    def from_gh_repo(gh_repo: Repository):
        return RadarRepo(name=gh_repo.full_name,
                         url=gh_repo.html_url,
                         stars=gh_repo.stargazers_count,
                         desc=gh_repo.description, topics=gh_repo.get_topics(),
                         forks=gh_repo.forks_count,
                         languages=gh_repo.get_languages())

    def to_json(self):
        return json.dumps(self.__dict__)

    def to_dict(self):
        return self.__dict__


class BaseGithubCollector(BaseCollector):

    def __init__(self, config=None):
        self.config = config
        self.gh = make_client()
