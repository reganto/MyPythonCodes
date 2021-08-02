class File:
    def __init__(self, filename, mode="rt"):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, mode=self.mode)
        return self.open_file

    def __exit__(self, *excepts):
        self.open_file.close()
