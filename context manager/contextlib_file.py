from contextlib import contextmanager


@contextmanager
def open_file(file_name, mode="rt"):
    my_file = open(file_name, mode=mode)
    yield my_file
    my_file.close()

    """
    everything before yield is __enter__ 
    and anything after yield is __exit__
    """


with open_file("/tmp/alaki.txt") as f:
    print(f.read())
