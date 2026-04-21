"""Tests for the geokyw package."""

import io
import unittest
from contextlib import redirect_stdout

from geokyw import __version__, format_greeting
from geokyw.cli import main


class TestGeokyw(unittest.TestCase):
    """Exercise the package through its public Python and CLI interfaces."""

    def test_format_greeting_uses_world_by_default(self):
        """The core helper should provide a sensible default greeting."""

        self.assertEqual(format_greeting(), "Hello, World!")

    def test_format_greeting_normalizes_blank_names(self):
        """Whitespace-only names should fall back to the default."""

        self.assertEqual(format_greeting("  Alice  "), "Hello, Alice!")
        self.assertEqual(format_greeting("   "), "Hello, World!")

    def test_cli_hello_command(self):
        """The hello command should print the greeting for the provided name."""

        stdout = io.StringIO()
        with redirect_stdout(stdout):
            exit_code = main(["hello", "--name", "Geo"])

        self.assertEqual(exit_code, 0)
        self.assertEqual(stdout.getvalue().strip(), "Hello, Geo!")

    def test_cli_without_args_shows_help(self):
        """Running the CLI without a subcommand should show help text."""

        stdout = io.StringIO()
        with redirect_stdout(stdout):
            exit_code = main([])

        self.assertEqual(exit_code, 0)
        self.assertIn("usage:", stdout.getvalue())
        self.assertIn("hello", stdout.getvalue())

    def test_cli_version_flag(self):
        """The version flag should print the package version and exit cleanly."""

        stdout = io.StringIO()
        with self.assertRaises(SystemExit) as context:
            with redirect_stdout(stdout):
                main(["--version"])

        self.assertEqual(context.exception.code, 0)
        self.assertEqual(stdout.getvalue().strip(), f"geokyw {__version__}")
