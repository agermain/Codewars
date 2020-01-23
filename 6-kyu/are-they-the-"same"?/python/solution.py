import math

def comp(array1, array2):
    print(array1, array2)
    if array1 is None or array2 is None:
        return False
    array1 = [abs(x) for x in array1]
    for num in array2:
        if math.sqrt(num) in array1:
            array1.remove(math.sqrt(num))
        else:
            return False
    return True
	