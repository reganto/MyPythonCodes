import sys


def binary_search(items, item):
    first, last = 0, len(items) - 1
    while first <= last:
        mid_point = (first + last) // 2  # find mid point index
        if items[mid_point] == item:     # best case
            return mid_point
        elif items[mid_point] > item:
            last = mid_point - 1
        else:
            first = mid_point + 1
    
    # if item not exist in items
    return -1

convert_to_list = lambda d: [int(number) for number in d[1: len(d)-1].split(', ')] 
print(binary_search(convert_to_list(sys.argv[1]), int(sys.argv[2])))

# python app.py "[12, 34, 45, 90, 123, 231, 579, 1921]" 1921
