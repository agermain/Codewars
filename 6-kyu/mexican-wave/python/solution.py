def wave(str):
    l = []
    for i, char in enumerate(str):
        if not char.isalpha():
            continue
        tmp = list(str)
        tmp[i] = tmp[i].upper()
        l.append("".join(tmp))
    return l