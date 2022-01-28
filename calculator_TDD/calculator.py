from app import OP


class Calculator:
    @staticmethod
    def sum(*args):
        return OP.sum(*args)

    @staticmethod
    def div(*args):
        return OP.div(*args)


    @staticmethod
    def mul(*args):
        return OP.mul(*args)

    @staticmethod
    def minus(*args):
        return OP.min(*args)