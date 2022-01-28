def minus_op(*args):
    """Minus of two numbers"""
    
    TOTAL = args[0]
    for number in args[1:]:
        TOTAL -= number

    return TOTAL