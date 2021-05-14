#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.maven.services import get_artifact_info


def test_get_artifact_info():
    result = get_artifact_info(g="com.google.code.gson", a="gson", v=None)
    assert len(result.json()) >= 1
