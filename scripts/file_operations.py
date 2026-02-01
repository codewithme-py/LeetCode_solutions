"""
File operations for the LeetCode solutions project.

This module provides functionality to:
- Create solution files for LeetCode problems
- Create corresponding test files
- Handle file path operations and directory creation
"""
import re
from pathlib import Path

from constants import (
    CREATED_SOLUTION_FILE_MSG,
    CREATED_TEST_FILE_MSG,
    FILE_ALREADY_EXISTS_MSG,
    FILENAME_SANITIZE_REGEX,
    SOLUTION_FILENAME_PATTERN,
    TEST_FILENAME_PATTERN,
)


def _create_file_with_pattern(
    problem_id: str,
    problem_title: str,
    target_dir: Path,
    filename_pattern: str,
    success_message: str,
) -> Path:
    """
    Create a file with the given pattern.

    Args:
        problem_id: The ID of the LeetCode problem
        problem_title: The title of the LeetCode problem
        target_dir: Directory where the file should be created
        filename_pattern: Pattern for the filename (e.g., '{}_{:04d}.py')
        success_message: Message to print on successful creation

    Returns:
        Path to the created file
    """
    target_dir.mkdir(exist_ok=True)
    lower_title = problem_title.lower()
    snake_case_title = re.sub(FILENAME_SANITIZE_REGEX, '_', lower_title).strip('_')
    filename_base = snake_case_title
    if filename_base and filename_base[0].isdigit():
        filename_base = 'problem_' + filename_base
    filename = filename_pattern.format(filename_base, int(problem_id))
    filepath = target_dir / filename
    with open(filepath, 'w'):
        pass
    print(success_message.format(filepath))
    return filepath


def _html_to_docstring(html_content: str) -> str:
    """
    Convert HTML content to a markdown-formatted docstring.
    """
    if not html_content:
        return ''
    content = (
        html_content.replace('&nbsp;', ' ')
        .replace('&lt;', '<')
        .replace('&gt;', '>')
        .replace('&quot;', '"')
        .replace('&apos;', "'")
        .replace('&#39;', "'")
    )
    content = re.sub(r'<p>', '', content)
    content = re.sub(r'</p>', '\n\n', content)
    content = re.sub(r'<br\s*/?>', '\n', content)
    content = re.sub(r'<ul>', '', content)
    content = re.sub(r'</ul>', '', content)
    content = re.sub(r'<li>', '- ', content)
    content = re.sub(r'</li>', '\n', content)
    content = re.sub(r'<strong>(.*?)</strong>', r'**\1**', content)
    content = re.sub(r'<b>(.*?)</b>', r'**\1**', content)
    content = re.sub(r'<em>(.*?)</em>', r'*\1*', content)
    content = re.sub(r'<code>(.*?)</code>', r'`\1`', content)
    content = re.sub(r'<pre>', '\n', content)
    content = re.sub(r'</pre>', '\n', content)
    content = re.sub(r'<img[^>]*src="([^"]*)"[^>]*>', r'![Image](\1)', content)
    content = re.sub(r'<[^>]+>', '', content)
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content.strip()


def _create_file_with_content(
    problem_id: str,
    problem_title: str,
    target_dir: Path,
    filename_pattern: str,
    success_message: str,
    file_content: str = None
) -> Path:
    """
    Create a file with specific content.
    """
    target_dir.mkdir(exist_ok=True)
    lower_title = problem_title.lower()
    snake_case_title = re.sub(FILENAME_SANITIZE_REGEX, '_', lower_title).strip('_')
    filename_base = snake_case_title
    if filename_base and filename_base[0].isdigit():
        filename_base = 'problem_' + filename_base
    filename = filename_pattern.format(filename_base, int(problem_id))
    filepath = target_dir / filename
    if filepath.exists() and filepath.stat().st_size > 0:
        print(FILE_ALREADY_EXISTS_MSG.format(filepath))
        return filepath
    with open(filepath, 'w') as f:
        if file_content:
            f.write(file_content)
    print(success_message.format(filepath))
    return filepath


def create_solution_file(
    problem_id: str,
    problem_title: str,
    solutions_dir: Path = None,
    code_snippet: str = None,
    content_html: str = None,
    difficulty: str = None
):
    """
    Create a solution file for the problem.

    If code_snippet and content_html are provided, the file is populated
    with the solution class and a docstring description.
    """
    if solutions_dir is None:
        project_root = Path(__file__).parent.parent
        solutions_dir = project_root / 'solutions'
    file_content = ''
    if code_snippet:
        docstring = ''
        if content_html:
            clean_desc = _html_to_docstring(content_html)
            docstring = f'''    """
    {problem_id}. {problem_title}
    {difficulty or ''}
    {clean_desc}
    """'''
            if 'class Solution:' in code_snippet:
                parts = code_snippet.split('class Solution:', 1)
                file_content = f'{parts[0]}class Solution:{docstring}\n{parts[1]}'
            else:
                file_content = code_snippet
        else:
             file_content = code_snippet
    return _create_file_with_content(
        problem_id,
        problem_title,
        solutions_dir,
        SOLUTION_FILENAME_PATTERN,
        CREATED_SOLUTION_FILE_MSG,
        file_content
    )


def create_test_file(
    problem_id: str,
    problem_title: str,
    tests_dir: Path = None,
    module_name: str = None,
    test_cases: str = None
):
    """
    Create a test file for the problem.

    If module_name and test_cases are provided, the file is populated
    with a test template and example test cases.
    """
    if tests_dir is None:
        project_root = Path(__file__).parent.parent
        tests_dir = project_root / 'tests'
    file_content = ''
    if module_name:
        file_content = f"""import pytest
from solutions.{module_name} import Solution

@pytest.mark.parametrize("args, expected", [
    # TODO: Add test cases
    # {test_cases if test_cases else "Copy test cases here"}
])
def test_solution(args, expected):
    sol = Solution()
    # TODO: Call specific method
    # assert sol.method(args) == expected
    pass
"""

    return _create_file_with_content(
        problem_id,
        problem_title,
        tests_dir,
        TEST_FILENAME_PATTERN,
        CREATED_TEST_FILE_MSG,
        file_content
    )
