import string

def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for c in alphabet:
        if c in s.lower():
            continue
        return False
    return True