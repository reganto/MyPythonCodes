class Music(object):
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        return obj
    
    def __init__(self, name):
        self.set_name(name)

    def set_name(self, name):
        if name:
            self.name = name

    def get_name(self):
        return self.name
