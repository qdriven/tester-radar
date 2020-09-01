# -*- coding:utf-8 -*-
import argparse
import json
import os
from pprint import pprint

BASE_PATH = os.path.abspath(__file__).split('favorite_cli.py')[0]
with open(BASE_PATH + 'resources.json', 'r') as f:
    configuration = json.load(f)

resource_base_path = BASE_PATH + configuration.get('resource_path')
categories = configuration.get("categories")


def add_category(category_name):
    if category_name is not None:
        categories.append(category_name)
    _write_config()


def remove_category(category_name):
    try:
        categories.remove(category_name)
        _write_config()
        print(categories)
    except:
        pass


def _write_config():
    with open(BASE_PATH + 'resources.json', 'w') as f:
        json.dump(configuration, f, ensure_ascii=False, indent=4)


class Favorite:
    def __init__(self):
        self.existing_resources = {}

    def record(self, category=None, url=None, desc=None):
        if url is None or desc is None or category is None:
            raise Exception("category, url or desc is not existing")
        if category not in categories:
            raise Exception("category is not correct, it should be {}"
                            .format(','.join(categories)))
        json_file_path = resource_base_path + '/' + category + '.json'
        print('json file is ' + json_file_path)
        md_file_path = resource_base_path + '/' + category + '.md'
        print('md file is ' + md_file_path)

        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as f:
                self.existing_resources = json.load(f)

        # update dict with url
        self.existing_resources[url] = desc
        with open(md_file_path, 'w') as f:
            f.write('# {category} Resources \n'.format(category=category))
            for url, desc in self.existing_resources.items():
                f.write('- [{desc}]({url})\n'.format(desc=desc, url=url))

        with open(json_file_path, 'w') as out_put_file:
            json.dump(self.existing_resources, out_put_file,
                      ensure_ascii=False, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", help="add category name")
    parser.add_argument("-l", help="list category names")
    parser.add_argument("-u", help="added url")
    parser.add_argument("-c", help="category name for url")
    parser.add_argument("-d", help="url description")
    args = parser.parse_args()

    if args.a:
        add_category(args.a)
    if args.l == 'all':
        pprint(categories)
    else:
        pprint("current dir is " + os.getcwd())
        pprint("category is " + args.c)
        pprint("url is " + args.u)
        pprint("description is " + args.d)
        Favorite().record(category=args.c, url=args.u, desc=args.d)
