import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} time to execute")
        return result
    return wrapper

# NOTE: "time.perf_counter" for benchmarking is more consice
