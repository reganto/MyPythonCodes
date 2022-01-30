def linear_search(our_list, item):
    """Linear search

    :param our_list: our list of items
    :type our_list: list
    :param item: item for search
    :type number: int or float or string
    """

    our_list_length = len(our_list)  # O(1) -> constant runtime
    for index in range(0, our_list_length):  # O(n), O(our_list_length) -> linear runtime
        if our_list[index] == item:
            return index
    return -1