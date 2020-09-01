# -*- coding:utf-8 -*-
from unittest import TestCase

from generators.gitbook import Gitbook


class TestGitbookGenerator(TestCase):

    def setUp(self):
        self.gitbook = Gitbook(book_name='evenhumble')

    def test_init_book(self):
        self.gitbook.init_book()
