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

if __name__ == "__main__":
    obj = Foo('bar')
    print(obj)

    print(obj.__dict__)
    obj.something()
    
    obj.__name = 'some name'
    print(obj.value)

    print(obj.__dict__)
