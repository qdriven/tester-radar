#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
collector command to receive command to get different data
using python python-fire lib: https://github.com/google/python-fire
"""
import atexit

import fire

from collectors.github.stars import GithubSelfStarredRepoCollector, STARRED_REPO_JSON_FILE
from extractors.supplement import write_to_json_file

collector = GithubSelfStarredRepoCollector()


def star_exit_handler():
    print("start to handle star system exit hook ......")
    write_to_json_file(collector.starred_repos, STARRED_REPO_JSON_FILE)


atexit.register(star_exit_handler)


class CollectorCommander(object):
    def gh_stars(self):
        try:
            collector.fetch_data()
        finally:
            print("this is in final block")

    def gh_topics(self):
        pass

    def gh_trending(self):
        pass

    def gh(self):
        self.gh_stars()
        self.gh_topics()
        self.gh_trending()


if __name__ == '__main__':
    fire.Fire(CollectorCommander)
