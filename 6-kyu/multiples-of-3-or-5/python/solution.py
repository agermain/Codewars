def solution(number):
    return sum([n for n in range(0, number) if n % 3 == 0 or n % 5 == 0])