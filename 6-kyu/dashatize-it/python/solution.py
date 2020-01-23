def dashatize(num):
    res = ""
    if num == None:
        return 'None'
    for char in str(num):
        if not char.isdigit():
            continue
        if int(char) % 2 != 0:
            res += "-" + char + "-"
        else:
            res += char
    return res.strip('-').replace("--", "-")