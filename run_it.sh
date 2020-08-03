#!/usr/bin/env bash

python collector_commander.py gh_stars  && cp -rf starred_repo.json data/github/starred && pytest tests/test_readme_render.py && cp tests/README.md .