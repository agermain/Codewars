def tickets(people):
    hundred = 0
    fifty = 0
    twentyfive = 0
    for p in people:
        if p == 100:
            hundred += 1
            if fifty >= 1 and twentyfive >= 1:
                fifty -= 1
                twentyfive -= 1
                continue
            elif twentyfive >= 3:
                twentyfive -= 3
                continue
            else:
                return "NO"
        elif p == 50:
            fifty += 1
            if twentyfive >= 1:
                twentyfive -= 1
                continue
            else:
                return "NO"
        else:
            twentyfive += 1
            continue
    return "YES"
