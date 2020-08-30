#!/usr/bin/env python
# -*- coding: utf-8 -*-


## READ JSON Files
## Getting All Repos With testing label and save to another json files

"""
1. Load JSON file
2. Get All Repos which have label testing/automation
"""
from feeds.extractors.supplement import load_json_file, write_to_json_file


class GithubRepoAnalyzer:

    def __init__(self, raw_json_file):
        self.raw_data_dict = load_json_file(raw_json_file)
        self.result_repos = []

    def filter_by(self, topic_keys: [str] = None) -> {}:
        for url, repo_detail in self.raw_data_dict.items():
            for topic_key in topic_keys:
                if topic_key in repo_detail['topics']:
                    self.result_repos.append(repo_detail)

        return self.result_repos


if __name__ == '__main__':
    result = GithubRepoAnalyzer("starred_repo.json").filter_by(
        ["testing", "test", "selenium", 'automation', 'diff', 'assertion'])
    write_to_json_file(result, "testing_repo.json")
