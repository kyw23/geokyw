"""Core helpers for the geokyw package."""


def format_greeting(name="World"):
    """Return a friendly greeting for the provided name.

    Empty or whitespace-only names fall back to ``"World"`` so callers do not
    have to handle that edge case on their own.
    """

    cleaned_name = name.strip()
    if not cleaned_name:
        cleaned_name = "World"

    return f"Hello, {cleaned_name}!"
