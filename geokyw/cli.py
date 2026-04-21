"""Command line interface for geokyw."""

import argparse

from geokyw import __version__
from geokyw.geokyw import format_greeting


def build_parser():
    """Create the top-level argument parser for the CLI."""

    parser = argparse.ArgumentParser(
        prog="geokyw",
        description="Small command line utilities for geokyw.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers(dest="command")

    hello_parser = subparsers.add_parser("hello", help="Print a friendly greeting.")
    hello_parser.add_argument(
        "--name",
        default="World",
        help="Name to greet. Defaults to World.",
    )

    return parser


def main(argv=None):
    """Run the CLI and return an exit code when possible."""

    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "hello":
        print(format_greeting(args.name))
        return 0

    parser.print_help()
    return 0
