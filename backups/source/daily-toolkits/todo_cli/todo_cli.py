# -*- coding:utf-8 -*-
import argparse
import json

import datetime
import os
from pprint import pprint

BASE_PATH = os.path.abspath(__file__).split('todo_cli.py')[0]
CURRENT_ID_FILE = 'current_id'
TODO_ITEMS_FILE = "todo_items.json"


def _get_write_current_id(file_name):
    pprint("current id file is " + file_name)
    with open(BASE_PATH+"/"+file_name, 'r') as f:
        current_id = int(f.readline(1))
    with open(BASE_PATH+"/"+file_name, 'w') as f:
        current_id += 1
        f.write(str(current_id))
    return current_id


def get_current_id(cid_file=None):
    if cid_file is None:
        cid_file = CURRENT_ID_FILE
    return _get_write_current_id(cid_file)


def rest_current_id():
    with open('current_id_test', 'w') as f:
        f.write("0")


def read_todo(todoitems_file='todo_items.json'):
    with open(BASE_PATH+"/"+todoitems_file, 'r') as f:
        todo_items = json.load(f)
    return todo_items


def get_incompleted_todo(todoitems_file='todo_items.json'):
    todo_items = read_todo(todoitems_file)['todos']
    return [item for item in todo_items if item['status'] != 'COMPLETED']


def complete_todo(id, todoitems_file='todo_items.json'):
    todo_items = read_todo(todoitems_file)
    _update_task_by_id(todo_items, id)
    _dump_todo_items(todo_items, todoitems_file)


def _update_task_by_id(tasks, id):
    for item in tasks['todos']:
        if item['id'] == id:
            item['status'] = 'COMPLETED'
            return True
    return False


def get_todo_by_id(id, todoitems_file='todo_items.json'):
    todo_items = read_todo(todoitems_file)
    result = [item for item in todo_items['todos'] if item['id'] == id]
    if len(result) > 0:
        return result[0]
    else:
        return None


def _dump_todo_items(todo_items, todoitems_file):
    with open(BASE_PATH+"/"+todoitems_file, 'w') as f:
        json.dump(todo_items, f, ensure_ascii=False, indent=4)


def add_todo(desc, category='test', saved_file='todo_items.json'):
    todo = {
        "id": get_current_id(),
        "description": desc,
        "start_time": datetime.datetime.now().isoformat(),
        "category": category,
        "status": 'STARTED'
    }
    todos = read_todo()
    todos['todos'].append(todo)
    _dump_todo_items(todos, saved_file)
    return todo


# todo options for python
"""
-d: todo: description
-l: list todos
-c: complete task by id
-g: todo category
"""

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", help="todo desc ")
    parser.add_argument("-l", help="list todo ", default='ALL')
    parser.add_argument("-g", help="todo category ", default='coding')
    parser.add_argument("-c",
                        help="todo id for completing, normally list the task first,then find the right task id to complete")

    args = parser.parse_args()
    if args.d and args.g:
        add_todo(desc=args.d, category=args.g)
    if args.l:
        pprint(get_incompleted_todo())
    if args.c:
        complete_todo(args.c)
