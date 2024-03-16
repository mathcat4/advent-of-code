"""
Handles commands and file structures.
"""

import argparse
from aoc.utils import structure
import os

argparser = argparse.ArgumentParser(
    prog="aoc", description="Helper commands for Advent of Code"
)
subparser = argparser.add_subparsers(title="subcommands", dest="subcommands")

start_parser = subparser.add_parser("start", help="Create template files for AOC")
start_parser.add_argument("day", nargs="?", type=int, help="Day to start")
start_parser.add_argument("year", nargs="?", type=int, help="Year to start")
start_parser.add_argument(
    "-f", "--force", action="store_true", help="Force rewrite files"
)
start_parser.add_argument(
    "-n", "--no-fetch", action="store_true", help="Don't fetch input file"
)

run_parser = subparser.add_parser("run", help="Run AOC file")
run_parser.add_argument("day", nargs="?", type=int, help="Day to run")
run_parser.add_argument("year", nargs="?", type=int, help="Year to run")

args = argparser.parse_args()

## Command "start"
if args.subcommands == "start":
    day, year = structure.parse_date(args.day, args.year)

    path = f"aoc/{year}/{day:02d}"
    os.makedirs(path, exist_ok=True)

    structure.rewrite_file(
        os.path.join(path, "part1.py"), structure.P1_TEMPLATE, args.force
    )

    structure.rewrite_file(
        os.path.join(path, "part2.py"), structure.P2_TEMPLATE, args.force
    )

    structure.rewrite_file(os.path.join(path, "test.txt"), "", args.force)

    aoc_input = "input"
    structure.rewrite_file(os.path.join(path, "inp.txt"), aoc_input, not args.no_fetch)

## Command "run"
if args.subcommands == "run":
    print("run")
