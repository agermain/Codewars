def high(x):
    # Code heredef high(x):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ans, ret = 0, ""
    for word in x.split():
        res = 0
        for char in word:
            res += alphabet.index(char)+1
        if res > ans:
            ans, ret = res, word
    return ret