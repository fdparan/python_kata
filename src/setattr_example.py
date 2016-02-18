from __future__ import print_function
from pprint import pprint

class Foo:
    class_var = "A class variable"
    def __init__(self, value):
        self.__value = value

    def __setattr__(self, name, value):
        print("Setting {} = {}".format(name, value))
        self.__dict__[name] = value

    def __str__(self):
        return '{}, {}'.format(self.__value, self.class_var)

    def __hidden(self):
        return "hidden"

if __name__ == "__main__":
    obj = Foo('bar')
    obj2 = Foo('bla')

    print(obj)
    print(obj2)

    print(obj.__dict__)
    print(vars(obj))

    print(obj.class_var)
    print(obj2.class_var)

    Foo.class_var = 'foo'
