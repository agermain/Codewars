def revrot(strng, sz):
    if sz <= 0 or not strng or sz > len(strng):
        return ""
    l = [strng[i: i + sz] for i in range(0, len(strng), sz)]
    for index, num in enumerate(l):
        if len(num) < sz:
            l.remove(num)
            continue
        current = 0
        for digit in [int(i) for i in num]: current += digit**3
        if current % 2 == 0:
            l[index] = num[::-1]
        else:
            l[index] = num[1:] + num[:1]
    return ''.join(l)
        