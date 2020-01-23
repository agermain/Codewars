def square_digits(num):
    ans = ""
    for char in str(num):
        num = int(char)
        ans += str(num*num)
    return int(ans)