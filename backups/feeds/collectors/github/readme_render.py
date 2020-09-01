#!/usr/bin/env python
# -*- coding: utf-8 -*-

from backups.feeds.extractors.supplement import load_json_file

html_escape_table = {
    ">": "&gt;",
    "<": "&lt;",
}


def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c, c) for c in text)


"""
language:
1. java/kotlin/scala
2. python
3. go
4. javascript/typescript
"""

category_map = {
    "JAVA": ["java", "scala", "kotlin"],
    "PYTHON": ["python"],
    "JAVASCRIPT": ["javascript", "typescript"],
    "GO": ["GO", "GOLANG"]
}

FILE_PATH = "/Users/Patrick/workspace/products/test-blog/tester-radar/data/github/starred"


class ReadmeRender:

    def __init__(self):
        self.repo_json = FILE_PATH + "/starred_repo.json"
        self.starred_repos = load_json_file(self.repo_json)
        self.topic_dict = {}
        self.languages_dict = {"JAVA": [], "PYTHON": [], "JAVASCRIPT": [], "GO": []}
        self.readme_lines = []

    def render_readme(self):
        for url, repo in self.starred_repos.items():
            self.add_to_category(repo)

        self.readme_lines.append("# README\n")
        for key, repos in self.languages_dict.items():
            self.readme_lines.append("## {}\n".format(key))
            for repo in repos:
                description = html_escape(repo.get("desc", "")).replace('\n', '') if repo.get("desc", "") else ''
                self.readme_lines.append("- [{}]({}) - {}\n".format(repo["name"], repo["url"], description))
        with open('README.md', "w") as rm:
            rm.writelines(self.readme_lines)

    def add_to_category(self, repo):
        for category_name in category_map.keys():
            for lang in repo.get("languages", []).keys():
                if lang.lower() in category_map[category_name]:
                    self.languages_dict[category_name.upper()].append(repo)
