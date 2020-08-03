# -*- coding:utf-8 -*-
from unittest import TestCase

from todo_cli import rest_current_id, get_current_id, add_todo, read_todo, complete_todo, get_incompleted_todo, \
    get_todo_by_id


class TestToDoCli(TestCase):
    def test_get_current_id(self):
        rest_current_id()
        cid = get_current_id('current_id_test')
        self.assertEqual(cid, 1)

    def test_add_todo(self):
        add_todo(category='java', desc="write a todo command line"
                 , saved_file='todo_items_test.json')
        todos = read_todo("todo_items_test.json")
        self.assertTrue(len(todos) >= 1)

    def test_complete_todo(self):
        complete_todo(id=2, todoitems_file='todo_items_test.json')
        self.assertEqual(get_todo_by_id(2, todoitems_file='todo_items_test.json')['status'], 'COMPLETED')

    def test_get_incomplete_task(self):
        self.assertTrue(len(get_incompleted_todo(todoitems_file='todo_items_test.json')) == 0)