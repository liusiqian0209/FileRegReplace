# -*- coding: utf-8 -*-

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

    def find_dict(self, path):
        return self.changelist.get(path)

    def new_dict(self, path, reg, replacement):
        entity = {reg: replacement}
        self.changelist[path] = entity

    # 对于一个新数据，如果path之前存在，则对应dict里增加reg与replacement的映射
    # 如果path是新的，先建立path对应的dict，然后再向dict里增加项
    def generate_map(self, path, reg, replacement):
        entity = self.find_dict(path)
        if entity is None:  # 新元素
            self.new_dict(path, reg, replacement)
        else:
            entity[reg] = replacement


if __name__ == '__main__':
    arr = FileRegRepl()
    arr.generate_map('path_aaa', '\d\d', '112')
    arr.generate_map('path_aaa', '\s\w', 'sb')
    arr.generate_map('path_bbb', '\d\s', '2 ')
    arr.generate_map('path_bbb', '{\w+}', '12')
    arr.generate_map('path_aaa', '\w', '2')
    arr.generate_map('path_ccc', 'ab\d', 'ab2')
    arr.generate_map('path_aaa', '\d\s', '113')
    print arr
