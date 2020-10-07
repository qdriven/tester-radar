#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

from fastapi import APIRouter

from . import models
from .services import get_artifact_info

maven_router = APIRouter()


@maven_router.get("/maven", response_model=models.AllArtifactsResponse)
def get_maven_repo(g: Optional[str] = None, a: Optional[str] = None, v: Optional[str] = None):
    if g is None and a is None:
        return models.AllArtifactsResponse()

    return get_artifact_info(g, a, v)
