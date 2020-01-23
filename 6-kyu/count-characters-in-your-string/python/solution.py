def count(string):
    d = {}
    for char in string:
        if char not in d.keys():
            d[char] = 0
        d[char] += 1
    return d