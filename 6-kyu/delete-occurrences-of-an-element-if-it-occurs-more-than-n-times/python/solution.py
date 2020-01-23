def delete_nth(order,max_e):
    d = {}
    l = []
    for n in order:
        d[n] = d.get(n, 0) + 1
        if d.get(n, 0) > max_e:
            continue
        l.append(n)
    return l