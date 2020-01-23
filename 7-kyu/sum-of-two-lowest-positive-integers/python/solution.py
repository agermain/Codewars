def sum_two_smallest_numbers(numbers):
    first = min(numbers)
    numbers.remove(first)
    second = min(numbers)
    return first+second