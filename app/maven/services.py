#!/usr/bin/env python
# -*- coding: utf-8 -*-
## normal search
# fetch("https://search.maven.org/classic/solrsearch/select?q=com.google.code.gson&rows=20&wt=json", {
#   "headers": {
#     "accept": "application/json, text/javascript, */*; q=0.01",
#     "accept-language": "zh-CN,zh;q=0.9",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "x-requested-with": "XMLHttpRequest",
#     "cookie": "__utma=15796916.578956780.1602076030.1602076030.1602076030.1; __utmc=15796916; __utmz=15796916.1602076030.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=15796916.7.10.1602076030"
#   },
#   "referrer": "https://search.maven.org/classic/",
#   "referrerPolicy": "strict-origin-when-cross-origin",
#   "body": null,
#   "method": "GET",
#   "mode": "cors"
# });

##
# fetch("https://search.maven.org/classic/solrsearch/select?q=g%3A%22com.google.code.gson%22%20AND%20a%3A%22gson%22&rows=20&wt=json", {
#   "headers": {
#     "accept": "application/json, text/javascript, */*; q=0.01",
#     "accept-language": "zh-CN,zh;q=0.9",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "x-requested-with": "XMLHttpRequest"
#   },
#   "referrer": "https://search.maven.org/classic/",
#   "referrerPolicy": "strict-origin-when-cross-origin",
#   "body": null,
#   "method": "GET",
#   "mode": "cors",
#   "credentials": "include"
# });
import urllib
from typing import Optional

import requests

from app.maven.models import AllArtifactsResponse, ArtifactResponse

maven_str_template = """<dependency><groupId>{groupId}</groupId><artifactId>{artifactId}</artifactId><version>{latestVersion}</version></dependency>"""
gradle_str_template = "implementation '{groupId}:{artifactId}: {latestVersion}'"


def get_artifact_info(g: Optional[str], a: Optional[str], v: Optional[str]) -> AllArtifactsResponse:
    search_params = []
    if g is not None:
        search_params.append("g:\"" + g + "\"")
    if a is not None:
        search_params.append("a:\"" + a + "\"")
    if v is not None:
        search_params.append("v:\"" + v + "\"")
    search_param_str = " AND ".join(search_params)
    search_url = "https://search.maven.org/classic/solrsearch/select?" + urllib.parse.urlencode({"q": search_param_str})
    print(search_url)
    response = requests.get(search_url)
    json_resp = response.json()
    docs = json_resp['response']['docs']
    all_artifacts = AllArtifactsResponse()
    if len(docs) >= 1:
        for item in docs:
            mvn_str = maven_str_template.format(groupId=item['g'], artifactId=item['a'],
                                                latestVersion=item['latestVersion'])
            gradle_str = gradle_str_template.format(groupId=item['g'], artifactId=item['a'],
                                                    latestVersion=item['latestVersion'])
            all_artifacts.artifacts.append(ArtifactResponse(maven_xml_str=mvn_str, gradle_str=gradle_str))
    return all_artifacts
