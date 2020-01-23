
def unique_in_order(iterable):
    stack = []
    if len(iterable) > 0:
        stack.append(iterable[0])
        for i in range(0, len(iterable)):
            if iterable[i] == stack[-1]:
                continue
            else:
                stack.append(iterable[i])
        print(stack)
    return stack