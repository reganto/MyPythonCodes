def counter():
    number = 0
    def wrapper():
        nonlocal number
        number += 1
        return number
    return wrapper

