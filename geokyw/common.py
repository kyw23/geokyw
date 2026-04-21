"""The common module contains common functions and classes used by the other modules."""

from geokyw.geokyw import format_greeting


def hello_world(name="World"):
    """Print a greeting and return it for convenience in scripts and tests."""

    greeting = format_greeting(name)
    print(greeting)
    return greeting
