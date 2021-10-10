class Book:
    _instance = None
    
    # new is static -> default
    def __new__(cls, *args, **kwargs):
        if cls._instance is not None:
            raise TypeError("single instance from Book")
        cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass

