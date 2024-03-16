"""
Helper file for helper module :p
"""

import re, os
from datetime import datetime

P1_TEMPLATE = """from aoc.utils import *

"""

P2_TEMPLATE = """from aoc.utils import *

"""


def parse_date(day: int, year: int) -> tuple[int, int]:
    """
    Check if date meets restrictions
    """
    if (
        year
        and year not in range(2015, datetime.now().year)
        or (day and day not in range(1, 32))
    ):
        raise ValueError("Argument doesn't meet day/year restrictions")

    day = day if day else datetime.now().day
    year = year if year else datetime.now().year
    return day, year


def rewrite_file(path: str, template: str, force: bool) -> None:
    """
    If file exists, create template file, else rewrite file only if force is True.
    """
    if not os.path.exists(path) or force:
        with open(path, "w") as file:
            file.write(template)
