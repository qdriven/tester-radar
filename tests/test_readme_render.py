#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collectors.github.readme_render import ReadmeRender

rm_render = ReadmeRender()


def test_render_readme():
    rm_render.render_readme()
