#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from app.endpoints import gh_endpoint

api_router = APIRouter()
api_router.include_router(gh_endpoint.router, tags=["github"])

