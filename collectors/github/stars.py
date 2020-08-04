#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from collectors.github.base import BaseGithubCollector, RadarRepo
from collectors.github.github_config import GITHUB_TOKEN
from extractors.supplement import load_json_file, write_dict_to_json_file

STARRED_REPO_JSON_FILE = "./starred_repo.json"


class GithubSelfStarredRepoCollector(BaseGithubCollector):
    __star_header = {
        "accept": "application/vnd.github.v3.star+json",
        "Authorization": "token " + GITHUB_TOKEN
    }
    __default_header = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "token " + GITHUB_TOKEN
    }

    def __init__(self, config=None):
        super(GithubSelfStarredRepoCollector, self).__init__(config)
        self.starred_repos = load_json_file(STARRED_REPO_JSON_FILE)
        self.new_star_repo = dict()
        self.loop_count = 500
        self.current_starred = 2500

    def before_fetch(self):
        super().before_fetch()

    def unstar_repo(self, full_name):
        unstar_url = "https://api.github.com/user/starred/" + full_name
        delete_rsp = requests.delete(unstar_url, headers=self.__default_header)
        return delete_rsp

    def fetch_data(self):
        repos = self.gh.get_user().get_starred()
        try:
            for repo in repos:
                if self.loop_count > 0:
                    try:
                        radar_repo = RadarRepo.from_gh_repo(repo)
                        if self.starred_repos.get(radar_repo.url, None) is None:
                            self.starred_repos[radar_repo.url] = radar_repo.to_dict()
                    except Exception as e:
                        print(repo.full_name, "has exception", e)
                else:
                    break
                self.unstar_repo(repo.full_name)
                print("unstar ", repo.full_name)
                print("about {} repo is on the queue".format(self.loop_count))
                self.loop_count -= 1
        except Exception as e:
            print(e)
        ## TODO: add to decorator to save
        write_dict_to_json_file(self.starred_repos, STARRED_REPO_JSON_FILE)

    def after_fetch(self):
        super().after_fetch()

    def fetch(self):
        super().fetch()


## ToDo:
## 1. Use Headless to unstar
## 2. Use Headless to get star information
if __name__ == '__main__':
    collector = GithubSelfStarredRepoCollector()
    collector.fetch_data()
