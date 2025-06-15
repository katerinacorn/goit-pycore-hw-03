from datetime import datetime, timedelta
from typing import List, Dict

DATE_FORMAT = "%Y.%m.%d"
DAYS_IN_WEEK = 7
SATURDAY = 5
SUNDAY = 6
WEEKEND_DAYS = (SATURDAY, SUNDAY)


def get_congratulation_date(birthday_date: datetime) -> datetime:
    """
    Returns the adjusted congratulation date.
    If the birthday falls on a weekend, shifts it to the following Monday.
    """
    weekday = birthday_date.weekday()

    if weekday in WEEKEND_DAYS:
        days_to_monday = timedelta(DAYS_IN_WEEK - weekday)
        return birthday_date + days_to_monday

    return birthday_date


def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Returns a list of upcoming birthday congratulations within the next 7 days.
    If a birthday falls on a weekend, it is moved to the following Monday.

    :param users: List of users with 'name' and 'birthday' in 'YYYY.MM.DD' format.
    :return: List of dicts with 'name' and 'congratulation_date' in 'YYYY.MM.DD' format.
    """

    if not isinstance(users, list):
        print("Invalid input: users must be a list of dictionaries.")
        return []

    today = datetime.today().date()
    users_to_congratulate = []

    for user in users:
        if not isinstance(user, dict):
            continue

        name = user.get("name")
        birthday = user.get("birthday")

        if not isinstance(name, str) or not isinstance(birthday, str):
            continue

        try:
            birthday_date = datetime.strptime(birthday, DATE_FORMAT).date()
            birthday_date_this_year = birthday_date.replace(year=today.year)

            congratulation_date = get_congratulation_date(birthday_date_this_year)
            days_to_congratulation = (congratulation_date - today).days

            if not 0 <= days_to_congratulation <= DAYS_IN_WEEK:
                continue

            user = {
                "name": name,
                "congratulation_date": congratulation_date.strftime(DATE_FORMAT),
            }

            users_to_congratulate.append(user)
        except ValueError:
            print("Incorrect date format: expected 'YYYY.MM.DD' format.")
            continue

    return users_to_congratulate


print("Running tests...")


def days_from_today(days: int) -> str:
    today = datetime.today().date()
    return (today.replace(year=2000) + timedelta(days=days)).strftime(DATE_FORMAT)


users = [
    {"name": "Alice", "birthday": days_from_today(0)},  # today
    {"name": "Carol", "birthday": "2000.06.18"},  #
    {"name": "Bob", "birthday": "2000.06.14"},  # Saturday
    {"name": "Nate", "birthday": "2000.03.14"},  # too late
    {"name": "Dave", "birthday": days_from_today(10)},  # too far
    {"name": "Eve", "birthday": "invalid_date"},  # invalid date
    {"name": "NotADict"},  # invalid users
]

users_to_congratulate = get_upcoming_birthdays(users)
print(users_to_congratulate)

assert isinstance(users_to_congratulate, list)
assert all("congratulation_date" in user for user in users_to_congratulate)

expected_names = {"Alice", "Bob", "Carol"}
actual_names = {user["name"] for user in users_to_congratulate}

assert actual_names == expected_names, f"Expected {expected_names}, got {actual_names}"

print("All tests passed.")
