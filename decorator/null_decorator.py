def say_hello():
    return "hello"


def null_decorator(func):
    return func


@null_decorator
def say_by():
    return "by"