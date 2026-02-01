"""
Script to update the README with LeetCode solutions statistics.

This module provides functionality to:
- Update the README with statistics about solved problems
- Generate progress bars showing completion rates by difficulty
- Create a table of solved problems with links
- Optionally force refresh the problem cache
"""
# ruff: noqa: E501, UP015
#!/usr/bin/env python3
import argparse
import re
import sys
from collections import Counter
from pathlib import Path

# Add the scripts directory to the path to allow imports
sys.path.append(str(Path(__file__).parent))

from constants import (
    FORCE_REFRESH_CACHE_HELP,
    LEETCODE_BASE_URL,
    UPDATE_README_DESCRIPTION,
    UPDATED_README_WITH_N_SOLVED_PROBLEMS_MSG,
)
from problem_cache import fetch_full_problems_cache, load_problems_cache
from utils import extract_problem_number, make_bar

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
CACHE_FILE = PROJECT_ROOT / 'problems_cache.json'


def _calculate_percentage(solved: int, total: int) -> float:
    """
    Calculate percentage of solved problems.

    Args:
        solved: Number of solved problems
        total: Total number of problems

    Returns:
        Percentage as a float (0-100)
    """
    return (solved / total * 100) if total else 0


def _format_difficulty_stats(
    difficulty: str, solved: int, total: int, bar: str
) -> str:
    """
    Format difficulty statistics line for README.

    Args:
        difficulty: Difficulty level ('Easy', 'Medium', 'Hard')
        solved: Number of solved problems
        total: Total number of problems
        bar: Progress bar string

    Returns:
        Formatted statistics string
    """
    emoji = {'Easy': '🟢', 'Medium': '🟡', 'Hard': '🔴'}[difficulty]
    percentage = _calculate_percentage(solved, total)
    return f'{emoji} **{difficulty}**: {solved} &nbsp; `{bar}` &nbsp; _({percentage:.1f}%)_'


def main():
    """
    Main function to update the README with LeetCode solutions statistics.

    This function:
    1. Parses command-line arguments
    2. Loads the problems cache (optionally forcing refresh)
    3. Counts solved problems by difficulty
    4. Generates statistics and progress bars
    5. Updates the README file with the new information
    """
    parser = argparse.ArgumentParser(description=UPDATE_README_DESCRIPTION)
    parser.add_argument('--force-refresh-cache', action='store_true',
                        help=FORCE_REFRESH_CACHE_HELP)
    args = parser.parse_args()
    solutions_dir = PROJECT_ROOT / 'solutions'
    readme_path = PROJECT_ROOT / 'README.md'
    if args.force_refresh_cache:
        problems = fetch_full_problems_cache()
    else:
        problems = load_problems_cache()
    solved_files = []
    solved_stats = {'Easy': 0, 'Medium': 0, 'Hard': 0}
    if solutions_dir.exists():
        for f in solutions_dir.iterdir():
            if f.is_file():
                num = extract_problem_number(f.name)
                if num and str(num) in problems:
                    problem_data = problems[str(num)]
                    if len(problem_data) == 3:
                        title, difficulty, _ = problem_data
                    else:
                        title, difficulty = problem_data
                    solved_files.append((num, title, difficulty, f.name))
                    solved_stats[difficulty] += 1
    solved_files.sort(key=lambda x: x[0])
    total_solved = sum(solved_stats.values())
    counter = Counter(info[1] for info in problems.values())
    total_stats = {
        'Easy': counter['Easy'],
        'Medium': counter['Medium'],
        'Hard': counter['Hard']
    }
    easy_bar = make_bar(solved_stats['Easy'], total_stats['Easy'])
    medium_bar = make_bar(solved_stats['Medium'], total_stats['Medium'])
    hard_bar = make_bar(solved_stats['Hard'], total_stats['Hard'])
    easy_part = _format_difficulty_stats(
        'Easy', solved_stats['Easy'], total_stats['Easy'], easy_bar
    ) + '  \n'
    medium_part = _format_difficulty_stats(
        'Medium', solved_stats['Medium'], total_stats['Medium'], medium_bar
    ) + '  \n'
    hard_part = _format_difficulty_stats(
        'Hard', solved_stats['Hard'], total_stats['Hard'], hard_bar
    )
    stats_md = (
        f'✅ **Total**: **{total_solved}**  \n'
        + easy_part
        + medium_part
        + hard_part
    )
    if solved_files:
        table_rows = []
        for num, title, difficulty, file_name in solved_files:
            leetcode_url = f'{LEETCODE_BASE_URL}/{title.lower().replace(" ", "-")}/'
            link_part = f'[{title}]({leetcode_url})'
            solution_link = f'`{file_name}`'
            solution_path = f'solutions/{file_name}'
            table_row_start = f'| {num} | {link_part} | {difficulty} | ['
            table_row_end = f'{solution_link}]({solution_path}) |'
            table_row = table_row_start + table_row_end
            table_rows.append(table_row)
        table_md = '\n'.join(table_rows)
    else:
        table_md = '| — | — | — | — |'
    table_with_details = (
        f'<details>\n<summary><b> Show all solved problems </b></summary>\n\n'
        '## Problems\n\n'
        '| # | Title | Difficulty | Solution |\n'
        '|---|-------|------------|----------|\n'
        f'{table_md}\n'
        '</details>'
    )
    with open(readme_path) as f:
        content = f.read()
    content = re.sub(
        r'(<!-- START_STATS -->\n).*?(<!-- END_STATS -->)',
        f'<!-- START_STATS -->\n{stats_md}\n<!-- END_STATS -->',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'(<!-- START_TABLE -->\n).*?(<!-- END_TABLE -->)',
        f'<!-- START_TABLE -->\n{table_with_details}\n<!-- END_TABLE -->',
        content,
        flags=re.DOTALL
    )
    with open(readme_path, 'w') as f:
        f.write(content)
    print(UPDATED_README_WITH_N_SOLVED_PROBLEMS_MSG.format(total_solved))


if __name__ == '__main__':
    main()
