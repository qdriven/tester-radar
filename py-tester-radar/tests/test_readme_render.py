#!/usr/bin/env python
# -*- coding: utf-8 -*-
from backups.feeds.collectors import ReadmeRender

rm_render = ReadmeRender()


def test_render_readme():
    rm_render.render_readme()
