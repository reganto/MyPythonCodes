def division(*args):
    """Division operation"""

    TOTAL = args[0]
    for number in args[1:]:
        TOTAL /= number
    return TOTAL