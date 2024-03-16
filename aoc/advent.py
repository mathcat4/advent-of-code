"""
Handles commands and file structures.
"""

import argparse
from pathlib import Path
from datetime import datetime
from aoc.utils import structure
import os
import re

argparser = argparse.ArgumentParser(
    prog="aoc", description="Helper commands for Advent of Code"
)
argparser.add_argument(
    "-s", "--start", help="create template file for aoc d[day]y[year, optional]."
)
argparser.add_argument(
    "-f", "--fetch", help="fetch input for aoc d[day]y[year, optional]."
)

args = argparser.parse_args()

## Command "start"
if args.start is not None:
    print("ok")
    day, year = structure.parse_date(args.start)

    # Create template files
    path = f"aoc/{year}/{day:02d}"
    os.makedirs(path, exist_ok=True)

    with open(os.path.join(path, "part1.py"), "w") as file:
        file.write(structure.P1_TEMPLATE)

    with open(os.path.join(path, "part2.py"), "w") as file:
        file.write(structure.P2_TEMPLATE)

    with open(os.path.join(path, "test.txt"), "a") as file:
        pass

    with open(os.path.join(path, "inp.txt"), "a") as file:
        pass

## Command "fetch"


print("Hi!")
