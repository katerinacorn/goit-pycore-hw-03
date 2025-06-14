from typing import Union
import re


INTERNATIONAL_CODE = "+380"
PATTERN = r"^(\+?38)?0?"


def normalize_phone(phone_number: str) -> Union[str, None]:
    """
    Normalizes a phone number to the '+380XXXXXXXXX' format.

     - Keeps only digits and the leading '+'.
     - Adds '+38' if missing.
     - Converts '380...' to '+380...'.

     :param phone_number: Raw phone number string in any format.
     :return: Normalized phone number as string.
    """

    if not isinstance(phone_number, str):
        print("Invalid input: expected a phone number string.")
        return None

    cleaned_phone_number = re.sub(r"(?!^)\+|[^\d+]", "", phone_number.strip())
    if cleaned_phone_number.startswith(INTERNATIONAL_CODE):
        return cleaned_phone_number

    normalized_phone_number = re.sub(PATTERN, INTERNATIONAL_CODE, cleaned_phone_number)

    return normalized_phone_number


print("Running tests...")

# Test case 1: Correct international format
assert normalize_phone("+380 44 123 4567") == "+380441234567"


# Test case 2: Number with parentheses and dashes
assert normalize_phone("(095) 234-5678\n") == "+380952345678"  # FIX IT

# Test case 3: Number without country code
assert normalize_phone("067\t123 4567") == "+380671234567"  # FIX IT

# Test case 4: Starts with '380' without '+'
assert normalize_phone("380501234567") == "+380501234567"

# Test case 5: Mixed symbols and +38 present
assert normalize_phone("    +38(050)123-32-34") == "+380501233234"

# Test case 6: Starts with operator code only
assert normalize_phone("     0503451234") == "+380503451234"  # FIX IT

# Test case 7: With brackets only
assert normalize_phone("(050)8889900") == "+380508889900"  # FIX IT

# Test case 8: '380' prefix with dashes
assert normalize_phone("38050-111-22-22") == "+380501112222"

# Test case 9: '380' prefix with spaces
assert normalize_phone("38050 111 22 11   ") == "+380501112211"

# Test case 10: Number with extra +
assert normalize_phone("+380 44 +123 4567") == "+380441234567"

# Test case 10: Number with characters
assert normalize_phone("+380 44 123 4567num") == "+380441234567"


print("All tests passed.")

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

normalized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери:", normalized_numbers)
