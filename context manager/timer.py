import time


class Timer:
    def __init__(self, title):
        self.title = title

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exctype, value, traceback):
        self.elapsed_time = time.time() - self.start_time
        print(f"{self.title} took {self.elapsed_time}")
        print(f"ExcType: {exctype}")
        print(f"Value: {value}")
        print(f"Traceback: {traceback}")
        return True



with Timer("Alaki"):
    time.sleep(3)
    raise TypeError("Error in context manager")
    print("after exception")

