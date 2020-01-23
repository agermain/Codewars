def reverse_words(text):
    # Reverse entire string, split it to a list, reverse the list to keep order
    # and join with single spaces (for double spaces, they are items within the list)
    return " ".join(text[::-1].split(" ")[::-1])