from collections import Iterable
from collections import Iterator
import time

class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象被称为 可迭代对象，即可以使用for循环，
        那么必须要实现 __iter__ 方法"""
        return ClassItertor(self)


class ClassItertor(object):

    def __init__(self, obj):
        self.obj = obj
        self.current_num = -1

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_num < len(self.obj.names)-1:

            self.current_num += 1
            return self.obj.names[self.current_num]
        else:
            raise StopIteration



classmate = Classmate()
classmate.add("老王")
classmate.add("张三")
classmate.add("李四")


print("判断 classmate 是否是可以迭代的对象：",
      isinstance(classmate, Iterable))
classmate_iterator = iter(classmate)
print("判断 classmate_iterator 是否是迭代器：",
      isinstance(classmate_iterator, Iterator))

# print(next(classmate_iterator))

for name in classmate:
    print(name)
    time.sleep(1)