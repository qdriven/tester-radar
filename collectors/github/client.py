#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from github import Github

from collectors.github import github_config


def make_default_gh_client_by_access_token():
    return make_gh_client_by_access_token(github_config.GITHUB_TOKEN)


def make_gh_client_by_access_token(access_token=None):
    if access_token:
        return Github(access_token)
    else:
        if len(github_config.GITHUB_TOKEN) == 0:
            raise AttributeError("Github Access Token is not set,please check it again in github_config.py")
        return Github(github_config.GITHUB_TOKEN)


def make_gh_client_by_name(user_name, password):
    return Github(user_name, password)


def make_default_gh_client():
    return Github(github_config.GITHUB_USER, github_config.GITHUB_PWS)


def make_client():
    return make_default_gh_client_by_access_token()
