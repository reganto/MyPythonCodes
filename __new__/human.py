class Human:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        output = repr(self.name).rjust(10) + \
            repr(self.age).rjust(5) + \
            repr(self.sex).rjust(10)
        return output
    
