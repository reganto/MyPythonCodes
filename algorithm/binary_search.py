def binary_search(our_list, target):
    first = 0
    last = len(our_list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if target == our_list[midpoint]:
            return midpoint
        if target > our_list[midpoint]:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return -1


result = binary_search(
    [number**2 for number in range(1, 11)],
    81
)
print(result)