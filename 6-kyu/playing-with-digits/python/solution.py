def dig_pow(n, p):
    ans = 0
    numberStr = str(n)
    for i in range(0, len(numberStr)):
        ans += pow(int(numberStr[i]), p)
        p += 1
    return ans/n if ans % n == 0 else -1