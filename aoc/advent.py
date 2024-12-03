"""
Handles commands and file structures.
"""

import argparse
from aoc.utils import structure
from dotenv import load_dotenv
import os

load_dotenv()

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

fetch_parser = subparser.add_parser("fetch", help="Fetch AOC input")
fetch_parser.add_argument("day", nargs="?", type=int, help="Day to fetch")
fetch_parser.add_argument("year", nargs="?", type=int, help="Year to fetch")

run_parser = subparser.add_parser("run", help="Run AOC")
run_parser.add_argument("part", nargs="?", type=int, help="Part to run")
run_parser.add_argument("day", nargs="?", type=int, help="Day to run")
run_parser.add_argument("year", nargs="?", type=int, help="Year to run")
run_parser.add_argument(
    "-r", "--real", action="store_true", help="Use real input instead of test input"
)

args = argparser.parse_args()

## Command "start"
if args.subcommands == "start":
    day, year = structure.parse_date(args.day, args.year)

    path = f"aoc/{year}/{day:02d}"
    os.makedirs(path, exist_ok=True)

    structure.rewrite_file(
        os.path.join(path, "part1.py"),
        structure.create_template(day, year, 1),
        args.force,
    )

    structure.rewrite_file(
        os.path.join(path, "part2.py"),
        structure.create_template(day, year, 2),
        args.force,
    )

    structure.rewrite_file(os.path.join(path, "test.txt"), "", args.force)
    structure.rewrite_file(os.path.join(path, "inp.txt"), "", args.force)

## Command "fetch"
if args.subcommands == "fetch":
    day, year = structure.parse_date(args.day, args.year)

    structure.rewrite_file(
        f"aoc/{year}/{day:02d}/inp.txt", structure.fetch_input(day, year), True
    )

## Command "run"
if args.subcommands == "run":
    day, year = structure.parse_date(args.day, args.year)
    (
        structure.run(2, day, year, real=args.real)
        if args.part == 2
        else structure.run(1, day, year, real=args.real)
    )
