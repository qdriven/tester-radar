#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   
#   Author  :  patrick 
#   Date    :  2020/2/16 
#   Desc    :  Base Collector Files

"""
Base Collector Class
"""
import logging


class BaseCollector:
    """
    Base Collector Class
    """
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate,sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
    collector_name = "collector"

    def __init__(self,config=None):
        self.config=config
        self.logger = logging.getLogger(self.collector_name)

    def before_fetch(self):
        pass

    def fetch_data(self):
        pass

    def after_fetch(self):
        pass

    def fetch(self):
        self.before_fetch()
        self.fetch_data()
        self.after_fetch()
