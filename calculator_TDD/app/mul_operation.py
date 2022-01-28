def multiply(*args):
    """Multiply two number"""

    TOTAL = 1
    for number in args:
        TOTAL *= number
    
    return TOTAL