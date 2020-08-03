# -*- coding:utf-8 -*-
import os
import subprocess

import generators


class Gitbook:
    """
    Init parameters samples
        book_info = {
            "book_author": "book_author",
            "book_desc": "book_desc",
            "book_author_site": "http://www.baidu.com",
            "book_sourcecode_url": "http://www.baidu.com",
            "book_name": "book_name"
        }

    GitBook Generator Based on following assumption
    1. every content folder as a topic
    2. every topic folder depth is less than 2
    3. every folder name is start with a index,and separated by '_'

    """

    def __init__(self, book_name='gitbook_name',
                 book_desc='gitbook_desc',
                 book_author='hedwig',
                 book_author_site='http://www.google.com',
                 book_sourcecode_url="http://www.google.com",
                 root_path=os.getcwd()):
        self.root_path = root_path
        self.book_info = {
            "book_author": book_author,
            "book_desc": book_desc,
            "book_author_site": book_author_site,
            "book_sourcecode_url": book_sourcecode_url,
            "book_name": book_name
        }

    def init_book(self):
        """
        1. touch summary.md
        2. touch README.md
        :return:
        """

        subprocess.run("mkdir -p " + '/'.join([self.root_path, self.book_info['book_name']]), shell=True)
        summary_path = '/'.join([self.root_path, self.book_info['book_name'], 'SUMMARY.md'])
        readme_path = '/'.join([self.root_path, self.book_info['book_name'], 'README.md'])
        book_json = '/'.join([self.root_path, self.book_info['book_name'], 'book.json'])
        config_json = '/'.join([self.root_path, self.book_info['book_name'], 'config.json'])

        subprocess.run("touch " + summary_path, shell=True)
        subprocess.run("touch " + readme_path, shell=True)
        generators.render_template_to_file('gitbook/book.json',
                                           self.book_info, book_json)
        generators.render_template_to_file('gitbook/config.json',
                                           self.book_info, config_json)

    def generate_book(self):
        pass
