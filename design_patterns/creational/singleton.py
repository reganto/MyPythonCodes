class SingletonDecorator:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None
    
    def __call__(self, *args, **kwarg):
        if self.instance == None:
            self.instance = self.klass(*args, **kwarg)
        return self.instance


class foo:
    def __init__(self, x=''):
        self.y=x
    
    def __str__(self):
        return self.y


foo = SingletonDecorator(foo)

x = foo('Ali')
y = foo('Nima')
z = foo('Sara')

print("\n", x, y, z)
print(x is y is z)
