import time
import sys
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, *kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"{func.__name__!r} executed in {elapsed_time:.4f}")
    return wrapper


@timer
def fun(number):
    result = 0
    for _ in range(number):
        result += _**2

fun(int(sys.argv[1]))
