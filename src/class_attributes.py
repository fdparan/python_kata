from __future__ import print_function

class Foo:
    class_var = "A class variable"
    
    def __init__(self, value=''):
        self.value = value
        self.__dict__['__name'] = 'Foo'

    def __setattr__(self, name, value):
        if name.startswith('__'):
            print ("Changing a private attribute is not allowed.")
            return

        print("Setting {} = {}".format(name, value))
        self.__dict__[name] = value

    def __str__(self):
        return 'Instance: {}, Class: {}'.format(self.value, self.class_var)

    def something(self):
        self.x = 3

class ChildFoo(Foo):
    def __init__(self):
        super().__init__('Child Foo')

class my_class:
    cls_attr = "foo"
    cls_lst = []

    def __init__(self, name, value):
        self.name = name
        self.value = value

class sub_class(my_class):
    def __init__(self, name, value):
        self.marco = "Polo"
        super().__init__(name, value)

def foo_example():
    obj = Foo('bar')
    print(obj)

    print(obj.__dict__)
    obj.something()
    
    obj.__name = 'some name'
    print(obj.value)

    print(obj.__dict__)

if __name__ == "__main__":
    my_cls_obj = my_class('spam', 'a lot')

    monty = sub_class("Python", "The Holy Grail")
    print(my_class.__dict__.keys())
    print(my_cls_obj.__dict__.keys())

    print(sub_class.__base__.__dict__.keys())
    print(monty.cls_attr)
    
    foo_example()
