def alphabet_position(text):
    s = ""
    for char in text.lower():
        if not char.isalpha():
            continue
        s += str(ord(char) - 96) + " "
    return s.strip(" ")