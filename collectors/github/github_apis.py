# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     github_apis
   Description :
   Author :        patrick
   date：          2019/4/8
   reference:
    - https://github.com/PyGithub/PyGithub
    - https://github.com/gitpython-developers/GitPython
-------------------------------------------------
   Change Activity:
                   2019/4/8:
-------------------------------------------------
"""
import time
from pprint import pprint

import requests

__author__ = 'patrick'

from .github_config import *

GITHUB_URL = "https://api.github.com/"



class GithubAPIV3:
    """
    Use Request to get stars, not a good way to use
    """
    __star_header = {
        "accept": "application/vnd.github.v3.star+json",
        "Authorization": "token " + GITHUB_TOKEN
    }
    __default_header = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "token " + GITHUB_TOKEN
    }

    def __init__(self, token=None, user=None, pwd=None):
        # if token is not None:
        self.__token = GITHUB_TOKEN
        # if user is not None:
        self.__user = GITHUB_USER
        # if pwd is not None:
        self.__pwd = pwd
        self._gh = Github(self.__token)

    def get_starred_repo(self, iteration_count: int = 100):
        # GET / user / starred
        # GET / users /: username / starred
        for index in range(1, iteration_count):
            response = requests.get("https://api.github.com/user/starred?" + "?page=2",
                                    headers=self.__star_header)
            # print(response.json())
            # starred_repos = self._gh.get_user()
            # for repo in starred_repos:
            #     print(repo)
            list = []
            for repo in response.json():
                pprint(repo['repo']['html_url'])
                list.append(repo['repo']['html_url'])
                self.unstar_repo(repo)

            with open('../../data/github/starred/starred_repo.txt', 'a') as f:
                f.writelines("\n".join(list))

            time.sleep(1)

    def unstar_repo(self, item: dict):
        unstar_url = "https://api.github.com/user/starred/" + item['repo']["full_name"]
        delete_rsp = requests.delete(unstar_url, headers=self.__default_header)
        return delete_rsp

    def get_my_repos(self):
        repos = self._gh.get_user().get_repos()
        for repo in repos:
            print(repo)


def login_github(self):
    headers = self.__default_header
    headers[self.__user] = self.__token
    resp = requests.get(GITHUB_URL, headers=headers)
    print(resp)


if __name__ == '__main__':
    v = GithubAPIV3()
    resp = v.get_starred_repo()
    print(resp)
