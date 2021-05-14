#!/usr/bin/env bash

CONFIG_FILES=".gitignore .pre-commit-config.yaml pytest.ini setup.py pyproject.toml .flake8"
CONFIG_FOLDERS=".github"


for CONFIG in ${CONFIG_FILES}
do
  cp ${CONFIG} python-template
done


for CONFIG in ${CONFIG_FOLDERS}
do
  cp -rf ${CONFIG} python-template
done

cp -rf python-template ~/workspace/products/configuration/qworkspace/templates
cd ~/workspace/products/configuration/qworkspace/
git add .
git commit -m "update python templates"
git push origin master