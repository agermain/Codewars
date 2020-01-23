from collections import Counter 
def duplicate_count(text):
    d = Counter(text.lower())
    ans = 0
    for i in d:
        if d[i] > 1:
            ans += 1
    return ans 
    