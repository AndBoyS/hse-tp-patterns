import datetime
from functools import partial

# Концепт используется в functools.partial

dates = [
    datetime.datetime(2024, 1, 1),
    datetime.datetime(2025, 6, 8),
    datetime.datetime(2023, 12, 25),
]


def format_date(dt: datetime.datetime, fmt: str) -> str:
    return dt.strftime(fmt)


format_as_ymd = partial(format_date, fmt="%Y-%m-%d")
formatted_dates = list(map(format_as_ymd, dates))

print(formatted_dates)
