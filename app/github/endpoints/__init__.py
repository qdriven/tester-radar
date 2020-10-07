#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import APIRouter

from app.github.endpoints import gh_endpoint

gh_api_router = APIRouter()
gh_api_router.include_router(gh_endpoint.router, tags=["github"])

