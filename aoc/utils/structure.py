"""
Helper file for helper module :p
"""

import re
from datetime import datetime

P1_TEMPLATE = """from aoc.utils import *

"""

P2_TEMPLATE = """from aoc.utils import *

"""


def parse_date(date: str) -> tuple[int, int]:
    """
    Parse date of format d[day]y[year, optional]
    """
    matches = re.finditer("d(?P<day>[0-9]+)(y(?P<year>[0-9]+))?", date)
    if not matches:
        raise SyntaxError("Argument doesn't match syntax d[day]y[year, optional]")

    years = []
    days = []
    for match in matches:
        day, year = match.group("day"), match.group("year")
        if day is not None:
            days.append(int(day))
        if year is not None:
            years.append(int(year))

    days = [day for day in days if 1 <= day <= 31]
    years = [year for year in years if 2015 <= year <= datetime.now().year]

    if not days:
        raise ValueError("Argument doesn't meet day/year restrictions")
    elif days and years:
        day = days[0]
        year = years[0]
    else:
        day = days[0]
        year = datetime.now().year
    return day, year
