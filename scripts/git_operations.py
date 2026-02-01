"""
Git operations for the LeetCode solutions project.

This module provides functionality to:
- Create git branches for new LeetCode problems
- Handle git operations for the project workflow
"""
import re
import subprocess

from constants import (
    BRANCH_EXISTS_MSG,
    BRANCH_NAME_PATTERN,
    CREATED_BRANCH_MSG,
    ERROR_CREATING_BRANCH_MSG,
    ERROR_CREATING_GIT_BRANCH_MSG,
    GIT_BRANCH_CMD,
    GIT_BRANCH_PATTERN_PREFIX,
    GIT_BRANCH_PATTERN_SUFFIX,
    GIT_CHECKOUT_CMD,
    GIT_CMD,
    GIT_CREATE_BRANCH_CMD,
    GIT_LIST_FLAG,
)


def create_git_branch(problem_id: str, problem_title: str):
    """
    Create a git branch for the problem.

    Args:
        problem_id: The ID of the LeetCode problem
        problem_title: The title of the LeetCode problem

    Returns:
        Name of the created branch or None if creation failed
    """
    formatted_title = problem_title.lower().replace(' ', '-')
    branch_name = BRANCH_NAME_PATTERN.format(formatted_title, int(problem_id))
    try:
        result = subprocess.run(
            [GIT_CMD, GIT_BRANCH_CMD, GIT_LIST_FLAG], capture_output=True, text=True
        )
        branch_pattern = (
            GIT_BRANCH_PATTERN_PREFIX
            + re.escape(branch_name)
            + GIT_BRANCH_PATTERN_SUFFIX
        )
        if re.search(branch_pattern, result.stdout, re.MULTILINE):
            print(BRANCH_EXISTS_MSG.format(branch_name))
            return branch_name
        cmd_args = [GIT_CMD, GIT_CHECKOUT_CMD, GIT_CREATE_BRANCH_CMD, branch_name]
        result = subprocess.run(cmd_args, capture_output=True, text=True)
        if result.returncode != 0:
            print(ERROR_CREATING_BRANCH_MSG.format(result.stderr))
            return None
        print(CREATED_BRANCH_MSG.format(branch_name))
        return branch_name
    except Exception as e:
        print(ERROR_CREATING_GIT_BRANCH_MSG.format(e))
        return None
