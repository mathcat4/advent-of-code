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
subparser = argparser.add_subparsers(title="subcommands", dest="subcommands")

start_parser = subparser.add_parser("start", help="Create template file for AOC")
start_parser.add_argument("day", nargs="?", type=int, help="Day to start")
start_parser.add_argument("year", nargs="?", type=int, help="Year to start")
start_parser.add_argument(
    "-f", "--force", action="store_true", help="Force rewrite files"
)

fetch_parser = subparser.add_parser("fetch", help="Fetch AOC input")
fetch_parser.add_argument("day", nargs="?", type=int, help="Day to fetch")
fetch_parser.add_argument("year", nargs="?", type=int, help="Year to fetch")

args = argparser.parse_args()

## Command "start"
if args.subcommands == "start":
    day, year = structure.parse_date(args.day, args.year)

    # Create template files
    path = f"aoc/{year}/{day:02d}"
    os.makedirs(path, exist_ok=True)

    structure.rewrite_file(
        os.path.join(path, "part1.py"), structure.P1_TEMPLATE, args.force
    )

    structure.rewrite_file(
        os.path.join(path, "part2.py"), structure.P2_TEMPLATE, args.force
    )

    structure.rewrite_file(os.path.join(path, "test.txt"), "", args.force)

    structure.rewrite_file(os.path.join(path, "inp.txt"), "", args.force)

## Command "fetch"


print("Hi!")
