def italic(func):
    def wrapper():
        original_result = func()
        modified_result = "<italic>" + original_result + "</italic>"
        return modified_result
    return wrapper


def bold(func):
    def wrapper():
        original_result = func()
        modified_result = "<bold>" + original_result + "</bold>"
        return modified_result
    return wrapper


