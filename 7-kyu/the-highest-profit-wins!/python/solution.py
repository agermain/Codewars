import sys
def min_max(lst):
    min = max = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < min:
            min = lst[i]
        if lst[i] > max:
            max = lst[i]
    return [min, max]