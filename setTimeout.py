import time

def set_timeout(func, timeout, *args, **kwargs):
    while True:
        func(*args, **kwargs)
        time.sleep(timeout)

