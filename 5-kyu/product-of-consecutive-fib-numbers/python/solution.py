def productFib(prod):    
    i = 0
    while True:
        current = fibonacci(i)*fibonacci(i+1)
        if prod > current:
            i+=1
            continue
        elif prod == current:
            return [fibonacci(i), fibonacci(i+1), True]
        else:
            return [fibonacci(i), fibonacci(i+1), False]
    return 
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a