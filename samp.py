class Test(object): 
    def __init__(self): 
        self.a = 'a'
        self.b = 'b'
        self.c = 'c'
    def __getattr__(self, name):
        print('Getting %s'%name)
        return 123456

if __name__ == "__main__":
    t = Test()
    print('object variables: %r' % t.__dict__.keys())
    print(t.a)
    print(t.b)
    print(t.c)
    print(t.__class__)
    print(getattr(t, 'd'))
    print(hasattr(t, 'x'))
