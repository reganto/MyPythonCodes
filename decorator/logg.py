from functools import wraps


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__ + "was called")
        return func(*args, **kwargs)
    return wrapper


@logged
def f(x):
    return x+x*x


print(f.__name__)
