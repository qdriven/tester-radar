# -*- coding:utf-8 -*-
from unittest import TestCase

from generators import render_template_to_file


class TestRender_template(TestCase):
    def test_render_template(self):
        book_info = {
            "book_author": "book_author",
            "book_desc": "book_desc",
            "book_author_site": "http://www.baidu.com",
            "book_sourcecode_url": "http://www.baidu.com",
            "book_name": "book_name"
        }

        render_template_to_file("gitbook/book.json", book_info)
        render_template_to_file("gitbook/config.json", book_info)
