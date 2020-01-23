import collections

def find_it(seq):
    count = collections.Counter(seq)
    for key, value in count.items():
        if value % 2 != 0:
            return key
    return None
