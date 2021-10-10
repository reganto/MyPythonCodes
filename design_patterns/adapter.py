# Design Pattern: Adapter
# Author: Reganto
# Blog: reganto

class A(object):
    def b(self):
        print("A.b")
    
    def c(self):
        print("A.c")
        

class B(object):
    def d(self):
        print("B.d")
        

class Adapter(A):
    def __init__(self, klass):
        self.klass = klass
        
    def fun(self):
        self.b()
        self.c()
        instance = self.klass()
        instance.d()


# Usage

obj = Adapter(B)
obj.fun()
