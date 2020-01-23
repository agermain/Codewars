def kebabize(string):
    ns = ""
    for i, char in enumerate(string):
        if char.isdigit():
            continue
        if char.isupper():
            ns += "-" + char.lower()
        else:
            ns += char
    return ns.strip("-")