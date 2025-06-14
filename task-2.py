from typing import List
import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> List[int]:
    """
    Generates a sorted list of unique random lottery numbers within a given range.

    :param min: Minimum possible number (must be ≥ 1).
    :param max: Maximum possible number (must be ≤ 1000).
    :param quantity: Number of unique numbers to generate (must fit in range).
    :return: List[int]: Sorted list of unique random numbers, or empty list if input is invalid.
    """

    if not all(isinstance(arg, int) for arg in (min, max, quantity)):
        print("Invalid input: all arguments must be integers.")
        return []

    if min < 1 or max > 1000:
        print("Invalid input: min must be at least 1, max must not exceed 1000.")
        return []

    if not (min <= quantity <= max):
        print(f"Invalid input: quantity must be in the range {min}-{max}.")
        return []

    numbers = random.sample(range(min, max), quantity)
    return sorted(numbers)


print("Running tests...")

# Test 1: Correct
numbers = get_numbers_ticket(1, 49, 6)
assert len(numbers) == 6
assert sorted(numbers) == numbers
assert len(set(numbers)) == len(numbers)

# Test 2: quantity out of the range
assert get_numbers_ticket(1, 5, 10) == []

# Test 3: min < 1
assert get_numbers_ticket(0, 49, 6) == []

# Test 4: max > 1000
assert get_numbers_ticket(1, 1001, 6) == []

# Test 5: min > max
assert get_numbers_ticket(50, 10, 5) == []

# Test 6: quantity = 0
assert get_numbers_ticket(1, 10, 0) == []

# Test 7: Invalid type of args
assert get_numbers_ticket("1", 10, 0) == []

print("All tests passed.")

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
