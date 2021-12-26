import functools

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_func(*args, **kwargs):
            if user["access_level"] == "admin":
                return func(*args, **kwargs)

        return secure_func
    return decorator

