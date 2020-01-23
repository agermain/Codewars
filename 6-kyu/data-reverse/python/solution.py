def data_reverse(data):
    l = []
    for n in range(0,len(data),8):
        l.append([data[n+x] for x in range(0,8)])
    flat_list = []
    for sublist in l[::-1]:
        for item in sublist:
            flat_list.append(item)
    return flat_list