def formatting(lowercase=False):
    def formatting_decorator(func):
        def wrapper(text=""):
            if lowercase:
                func(text.lower())
            else:
                func(text.upper())
        return wrapper
    return formatting_decorator


@formatting(lowercase=False)
def chaap(message):
    print(message)


chaap("i love python")