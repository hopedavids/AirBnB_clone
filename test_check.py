#!/usr/bin/python3

"""
A module to test pycodstyle
"""
import models

def calculate_sum(numbers):
    """
    Calculates the sum of a list of numbers.

    Args:
        numbers: A list of numbers.

    Returns:
        The sum of the numbers in the list.
    """
    total = 0
    for num in numbers:
        total += num
    return total

numbers_list = [1, 2, 3, 4, 5]
result = calculate_sum(numbers_list)
print(result)
