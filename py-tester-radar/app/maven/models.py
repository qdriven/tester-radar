#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

from pydantic.main import BaseModel


class ArtifactResponse(BaseModel):
    maven_xml_str: str
    gradle_str: str


class AllArtifactsResponse(BaseModel):
    artifacts: List[ArtifactResponse] = []
