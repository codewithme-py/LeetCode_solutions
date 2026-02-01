"""
Script to create a new LeetCode problem solution.

This module provides functionality to:
- Create a new solution file for a specified LeetCode problem
- Create a corresponding test file
- Create a git branch for the new solution
- Validate that the problem exists in the cache
- Fetch problem details (description, snippets, tests) from LeetCode API

Usage:
    python create_problem.py <problem_id>
"""
import argparse
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from constants import (
    CACHE_OUTDATED_WARNING_MSG,
    CREATE_NEW_LEETCODE_PROBLEM_DESCRIPTION,
    CREATED_SOLUTION_AT_MSG,
    CREATED_TEST_AT_MSG,
    CREATING_SOLUTION_FOR_PROBLEM_MSG,
    ERROR_FETCHING_DETAILS_MSG,
    FAILED_TO_CREATE_GIT_BRANCH_MSG,
    FETCHING_PROBLEM_DETAILS_MSG,
    PROBLEM_ID_ARG_HELP,
    PROBLEM_NOT_FOUND_IN_CACHE_MSG,
)
from file_operations import create_solution_file, create_test_file
from git_operations import create_git_branch
from problem_cache import fetch_problem_data, load_problems_cache


def main():
    """
    Main function to create a new LeetCode problem solution.

    This function:
    1. Parses the command-line arguments
    2. Loads the problems cache
    3. Validates that the problem exists in the cache
    4. Creates a git branch for the new solution
    5. Fetches problem data from LeetCode API
    6. Creates the solution file with docstrings
    7. Creates the test file with test cases
    """
    parser = argparse.ArgumentParser(
        description=CREATE_NEW_LEETCODE_PROBLEM_DESCRIPTION
    )
    parser.add_argument('problem_id', type=str, help=PROBLEM_ID_ARG_HELP)
    args = parser.parse_args()
    problems = load_problems_cache()
    if args.problem_id not in problems:
        print(PROBLEM_NOT_FOUND_IN_CACHE_MSG.format(args.problem_id))
        return
    problem_data = problems[args.problem_id]
    if len(problem_data) == 3:
        title, difficulty, _ = problem_data
    else:
        title, difficulty = problem_data
    print(
        CREATING_SOLUTION_FOR_PROBLEM_MSG.format(
            args.problem_id, title, difficulty
        )
    )
    branch_name = create_git_branch(args.problem_id, title)
    if not branch_name:
        print(FAILED_TO_CREATE_GIT_BRANCH_MSG)
        return
    print(FETCHING_PROBLEM_DETAILS_MSG.format(title))
    try:
        if len(problems[args.problem_id]) == 3:
             _, _, title_slug = problems[args.problem_id]
             fetched_data = fetch_problem_data(title_slug)
             content_html = fetched_data.get('content')
             code_snippets = fetched_data.get('codeSnippets', [])
             code_snippet = next(
                 (s['code'] for s in code_snippets if s['langSlug'] == 'python3'), None
             )
             test_cases = fetched_data.get('exampleTestcases')
        else:
            print(CACHE_OUTDATED_WARNING_MSG)
            content_html = None
            code_snippet = None
            test_cases = None
    except Exception as e:
        print(ERROR_FETCHING_DETAILS_MSG.format(e))
        content_html = None
        code_snippet = None
        test_cases = None
    solution_path = create_solution_file(
        args.problem_id,
        title,
        code_snippet=code_snippet,
        content_html=content_html,
        difficulty=difficulty
    )
    test_path = create_test_file(
        args.problem_id,
        title,
        module_name=solution_path.stem,
        test_cases=test_cases
    )
    print(CREATED_SOLUTION_AT_MSG.format(solution_path))
    print(CREATED_TEST_AT_MSG.format(test_path))


if __name__ == '__main__':
    main()
