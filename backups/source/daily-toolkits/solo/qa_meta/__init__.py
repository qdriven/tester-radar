# -*- coding:utf-8 -*-

class Options:
    options = {}

    def __init__(self):
        pass

    def __getattr__(self, item):
        if self.options.get(item) is None:
            if hasattr(self, item):
                return getattr(self, item)
            else:
                self.__setattr__(item, '')
                return ''
        else:
            return self.options[item]

    def __setattr__(self, key, value):
        self.options[key] = value
