from datetime import datetime
from datetime import date
from datetime import timedelta


def get_week_start_date(desired_date: date) -> date:

    """Gets the start date (saturday) of the week that contains the desired date"""
    try:
        week_start_date = desired_date - timedelta(days=desired_date.weekday() + 2)
        return week_start_date
    except Exception as e:
        raise
