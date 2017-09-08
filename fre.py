# -*- coding: utf-8 -*-
import os
import re


class FileRegRepl(object):
    __slots__ = '__list'

    def __init__(self):
        self.__list = {}

    def __call__(self):
        pass

    def __str__(self):
        return self.changelist.__str__()

    __repr__ = __str__

    @property
    def changelist(self):
        return self.__list

    def __find_dict(self, path):
        return self.changelist.get(path)

    def __new_dict(self, path, reg, replacement):
        entity = {reg: replacement}
        self.changelist[path] = entity

    # 对于一个新数据，如果path之前存在，则对应dict里增加reg与replacement的映射
    # 如果path是新的，先建立path对应的dict，然后再向dict里增加项
    def reg_replace(self, path, reg, replacement):
        entity = self.__find_dict(path)
        if entity is None:  # 新元素
            self.__new_dict(path, reg, replacement)
        else:
            entity[reg] = replacement
        return self

    def __replace(self, line, repls):
        for key, value in repls.items():
            line = re.sub(key, value, line)
        return line

    def __readLines(self, path, repls):
        linelist = []
        if os.path.exists(path):
            file = open(path)
            iter_file = iter(file)
            for line in iter_file:
                newline = self.__replace(line, repls)
                linelist.append(newline)
            file.close()
        return linelist

    def __writeLines(self, filepath, lines):
        file = open(filepath, 'w')
        for line in lines:
            file.write(line)
        file.close()

    def __process_single_file(self, filepath, repls):
        lines = self.__readLines(filepath, repls)
        self.__writeLines(filepath, lines)

    def run(self):
        for path, repls in self.__list.items():
            self.__process_single_file(path, repls)


if __name__ == '__main__':
    FileRegRepl().reg_replace('Test.java', 'y = \d+', 'y = 35').reg_replace('Test.java', r'y[\s]?(\+|-|/)[\s]?x', 'y * x').reg_replace(
        'Test.java', 'World', 'liusiqian').reg_replace('test2.txt', 'score:\d+', 'score:100').run()
