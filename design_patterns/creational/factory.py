# Design Pattern: Factory
# Auther: Reganto
# Blog: reganto.ir


class Shirt(object):
    def __init__(self):
        self._color = None
        self._size = None

    @property
    def color(self):
        return self._color

    @property
    def size(self):
        return self._size


class Shirt_A(Shirt):
    def __init__(self):
        self._color = "Blue"
        self._size = "XL"
        

class Shirt_B(Shirt):
    def __init__(self):
        self._color = "Red"
        self._size = "M"


class Factory(object):
    @staticmethod
    def get_shirt(type_of_shirt):
        if type_of_shirt == "A":
            return Shirt_A()
        else:
            return Shirt_B()


class Store(object):
    def __init__(self, order_type):
        self._order_type = order_type
        
    @property
    def order_type(self):
        return self._order_type
    
    def order(self):
        f = Factory()
        shirt_object = f.get_shirt(self._order_type)
        return shirt_object
