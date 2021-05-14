# -*- coding:utf-8 -*-
import unittest

from favorite_cli import BASE_PATH, resource_base_path, categories, add_category, remove_category


class TestFavoriteCli(unittest.TestCase):
    def test_basepath(self):
        assert "daily-toolkits/favorite/" in BASE_PATH

    def test_resource_path(self):
        assert "daily-toolkits/favorite/resources" in resource_base_path

    def test_categories(self):
        assert "mooc" in categories
        assert isinstance(categories,list)

    def test_add_category(self):
        add_category("test")
        assert "test" in categories
        remove_category("test")
        assert "test" not in categories