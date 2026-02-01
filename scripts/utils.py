"""
Utility functions for the LeetCode solutions project.

This module provides utility functions for:
- Extracting problem numbers from file names
- Generating text-based progress bars
"""
import re

from constants import BAR_WIDTH, PROBLEM_NUMBER_REGEX


def extract_problem_number(file_name: str) -> int | None:
    """
    Extract problem number from file name.

    Args:
        file_name: The name of the file to extract the problem number from

    Returns:
        The extracted problem number or None if not found
    """
    if not file_name.endswith('.py'):
        return None
    if match := re.search(PROBLEM_NUMBER_REGEX, file_name):
        return int(match.group(1))
    return None


def make_bar(value: int, max_val: int, width: int = BAR_WIDTH) -> str:
    """
    Generate a text progress bar.

    Args:
        value: The current value
        max_val: The maximum value
        width: The width of the progress bar (default: BAR_WIDTH)

    Returns:
        A string representation of the progress bar
    """
    if max_val == 0:
        return '░' * width
    percentage = value / max_val
    filled = min(width, max(0, int(percentage * width)))
    empty = width - filled
    return '█' * filled + '░' * empty
