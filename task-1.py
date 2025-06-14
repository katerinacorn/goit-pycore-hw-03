from datetime import datetime, timedelta
from typing import Union

DATE_FORMAT = "%Y-%m-%d"


def get_days_from_today(date_string: str) -> Union[int, None]:
    """
    Calculates the number of days between today and the given date.

    :param date_string: A string in 'YYYY-MM-DD' format.
    :type date_string: str
    :return: Number of days difference.
             Negative if the date is in the future.
             None if the input is invalid.
    :rtype: int or None
    """

    if not isinstance(date_string, str):
        print("Invalid input: expected a string in 'YYYY-MM-DD' format.")
        return None

    try:
        input_date = datetime.strptime(date_string, DATE_FORMAT).date()
        today = datetime.today().date()
        delta = today - input_date
        return delta.days
    except ValueError:
        print("Incorrect date format: expected 'YYYY-MM-DD' format.")
        return None


print("Running tests...")

# Test case 1: today
today = datetime.today()
assert get_days_from_today(today.strftime(DATE_FORMAT)) == 0

# Test case 2: past date (1 day ago)
past_date = (today - timedelta(days=1)).strftime(DATE_FORMAT)
assert get_days_from_today(past_date) == 1

# Test case 3: future date (1 day ahead)
future_date = (today + timedelta(days=1)).strftime(DATE_FORMAT)
assert get_days_from_today(future_date) == -1

# Test case 4: invalid date format
assert get_days_from_today("2024/12/01") is None

# Test case 5: input is not a string
assert get_days_from_today(12345) is None

# Test case 6: empty string
assert get_days_from_today("") is None

print("All tests passed.")
