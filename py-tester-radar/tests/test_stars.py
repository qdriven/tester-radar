#!/usr/bin/env python
# -*- coding: utf-8 -*-
from backups.feeds.collectors import GithubSelfStarredRepoCollector


class TestGithubSelfStarredRepoCollector:
    def setup(self):
        self.collector = GithubSelfStarredRepoCollector()

    def test_fetch_data(self):
        print("start testing")
        self.collector.fetch_data()
        print("end of testing")

    def test_unstar_repo(self):
        # 'https://api.github.com/user/starred/mdrichardson/FUTpuppeteer'
        resp = self.collector.unstar_repo("mdrichardson/FUTpuppeteer")
        print(resp)
