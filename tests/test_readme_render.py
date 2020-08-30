#!/usr/bin/env python
# -*- coding: utf-8 -*-
from feeds.collectors.github import ReadmeRender

rm_render = ReadmeRender()


def test_render_readme():
    rm_render.render_readme()
