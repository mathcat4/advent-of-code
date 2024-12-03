"""
Helper file for the helper module :p
"""

import os
from datetime import datetime
from importlib import import_module
import requests


def create_template(day: int, year: int, part: int) -> str:
    template = (
        f'"""Day {day}, {year}, Part {part}"""\n'
        "\n"
        "from aoc.utils import *\n"
        "\n"
        "def main(inp):\n"
        "    return inp\n"
        "\n"
    )
    return template


def parse_date(day: int, year: int) -> tuple[int, int]:
    """
    Check if date meets restrictions
    """
    if (
        year
        and year not in range(2015, datetime.now().year + 1)
        or (day and day not in range(1, 26))
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


def fetch_input(day: int, year: int) -> str:
    session = os.environ.get("SESSION")
    response = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": session}
    )
    if not response.ok:
        raise RuntimeError(
            f"Request failed, code: {response.status_code}, message: {response.content}"
        )
    return response.text


def run(part: int, day: int, year: int, real: bool = True):
    if real:
        module = import_module(f"aoc.{year}.{day:02d}.part{part}")
        out = module.main(open(f"aoc/{year}/{day:02d}/inp.txt").read().strip())
        print(f"\033[1;31m{out}\033[0m")
    else:
        module = import_module(f"aoc.{year}.{day:02d}.part{part}")
        out = module.main(open(f"aoc/{year}/{day:02d}/test.txt").read().strip())

        print(f"\033[1;31m{out}\033[0m")
