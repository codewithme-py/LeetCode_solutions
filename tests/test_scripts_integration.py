"""
Integration tests for the scripts functionality.

This module tests the end-to-end functionality of the automation scripts:
- create_problem.py
- update_readme.py
- Various helper functions
"""
import datetime
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

# Add scripts directory to path so that 'import constants' works within scripts
sys.path.append(str(Path(__file__).parent.parent / 'scripts'))

import scripts.problem_cache as pc
import scripts.update_readme as ur
from scripts.create_problem import main as create_problem_main
from scripts.file_operations import create_solution_file, create_test_file
from scripts.file_operations import create_solution_file as orig_create_solution_file
from scripts.file_operations import create_test_file as orig_create_test_file
from scripts.git_operations import create_git_branch
from scripts.problem_cache import load_problems_cache
from scripts.update_readme import main as update_readme_main
from scripts.utils import extract_problem_number, make_bar


def test_load_problems_cache():
    """Test that the problem cache loads correctly."""
    problems = load_problems_cache()
    assert isinstance(problems, dict)
    assert len(problems) > 0
    for problem_id, data in problems.items():
        assert len(data) >= 2
        title = data[0]
        difficulty = data[1]
        assert isinstance(problem_id, str)
        assert isinstance(title, str)
        assert isinstance(difficulty, str)
        assert difficulty in ['Easy', 'Medium', 'Hard']


def test_load_problems_cache_failure_fallback(monkeypatch):
    """Test fallback to existing cache when update fails."""
    mock_cache_data = {'1': ['Two Sum', 'Easy', 'two-sum']}
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
        json.dump(mock_cache_data, tmp)
        tmp_path = Path(tmp.name)
    try:
        old_time = datetime.datetime.now() - datetime.timedelta(weeks=2)
        os.utime(tmp_path, (old_time.timestamp(), old_time.timestamp()))
        monkeypatch.setattr(pc, 'CACHE_FILE', tmp_path)
        def mock_fetch_fail():
            raise Exception("Network error")
        monkeypatch.setattr(
            pc, 'fetch_full_problems_cache', mock_fetch_fail
        )
        problems = pc.load_problems_cache()
        assert problems == mock_cache_data
    finally:
        if tmp_path.exists():
            os.unlink(tmp_path)


def test_extract_problem_number():
    """Test extracting problem numbers from file names."""
    assert extract_problem_number('two_sum_0001.py') == 1
    assert extract_problem_number('palindrome_number_0009.py') == 9
    assert extract_problem_number('invalid_file.txt') is None
    assert extract_problem_number('no_number.py') is None
    assert extract_problem_number('problem_123_test.py') is None


def test_make_bar():
    """Test the progress bar generation."""
    # Test normal cases
    assert make_bar(0, 10) == '░░░░░░░░░░'
    assert make_bar(10, 10) == '██████████'
    assert make_bar(5, 10) == '█████░░░░░'
    assert make_bar(0, 0) == '░░░░░░░░░░'
    assert make_bar(-5, 10) == '░░░░░░░░░░'
    assert make_bar(15, 10) == '██████████'


def test_create_solution_and_test_files():
    """Test creating solution and test files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        solution_path = create_solution_file('1', 'Two Sum', temp_path / 'solutions')
        test_path = create_test_file('1', 'Two Sum', temp_path / 'tests')
        assert solution_path.exists()
        assert test_path.exists()
        assert 'two_sum_0001.py' in str(solution_path)
        assert 'test_two_sum_0001.py' in str(test_path)


def test_create_git_branch(monkeypatch):
    """Test creating a git branch (if in a git repo)."""
    def mock_run(*args, **kwargs):
        class MockResult:
            def __init__(self):
                self.returncode = 0
                self.stdout = ""
                self.stderr = ""
        return MockResult()

    monkeypatch.setattr('scripts.git_operations.subprocess.run', mock_run)
    result = create_git_branch('999', 'Test Problem')
    assert result == 'feat/test-problem-0999'


def test_update_readme_script():
    """Test the update_readme script functionality."""
    temp_dir = Path(tempfile.mkdtemp())
    readme_path = temp_dir / 'README.md'
    with open(readme_path, 'w') as f:
        f.write("""# Test README

<!-- START_STATS -->
<!-- END_STATS -->

<!-- START_TABLE -->
<!-- END_TABLE -->
""")

    try:
        original_argv = sys.argv
        sys.argv = ['update_readme.py']
        original_project_root = ur.PROJECT_ROOT
        ur.PROJECT_ROOT = temp_dir
        ur.CACHE_FILE = original_project_root / 'problems_cache.json'
        update_readme_main()
        sys.argv = original_argv
        ur.PROJECT_ROOT = original_project_root
        with open(readme_path) as f:
            content = f.read()
            assert '<!-- START_STATS -->' in content
            assert '<!-- END_STATS -->' in content
            assert '<!-- START_TABLE -->' in content
            assert '<!-- END_TABLE -->' in content
            assert '✅ **Total**:' in content
    finally:
        shutil.rmtree(temp_dir)


class TestCreateProblemScript:
    """Test the create_problem script functionality."""

    def setup_method(self):
        """Set up temporary directories for testing."""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.original_cwd = Path.cwd()
        os.chdir(self.temp_dir)
        (self.temp_dir / 'solutions').mkdir(exist_ok=True)
        (self.temp_dir / 'tests').mkdir(exist_ok=True)

    def teardown_method(self):
        """Clean up temporary directories."""
        os.chdir(self.original_cwd)
        shutil.rmtree(self.temp_dir)

    def test_create_problem_script(self, monkeypatch):
        """Test the create_problem script main function."""
        original_argv = sys.argv
        sys.argv = ['create_problem.py', '1']
        try:
            def mock_load_problems_cache():
                return {
                    '1': ('Two Sum', 'Easy', 'two-sum')
                }
            def mock_fetch_problem_data(title_slug):
                return {
                    'content': '<p>Description</p>',
                    'codeSnippets': [
                        {'langSlug': 'python3', 'code': 'class Solution: pass'}
                    ],
                    'exampleTestcases': '[1,2]'
                }
            def mock_create_git_branch(problem_id, problem_title):
                return f'feat/two-sum-{int(problem_id):04d}'
            def mock_create_solution_file(problem_id, title, **kwargs):
                return orig_create_solution_file(
                    problem_id,
                    title,
                    solutions_dir=Path(self.temp_dir) / 'solutions',
                    **kwargs
                )
            def mock_create_test_file(problem_id, title, **kwargs):
                return orig_create_test_file(
                    problem_id,
                    title,
                    tests_dir=Path(self.temp_dir) / 'tests',
                    **kwargs
                )
            monkeypatch.setattr(
                'scripts.create_problem.load_problems_cache', mock_load_problems_cache
            )
            monkeypatch.setattr(
                 'scripts.create_problem.fetch_problem_data', mock_fetch_problem_data
            )
            monkeypatch.setattr(
                'scripts.create_problem.create_git_branch', mock_create_git_branch
            )
            monkeypatch.setattr(
                'scripts.create_problem.create_solution_file', mock_create_solution_file
            )
            monkeypatch.setattr(
                'scripts.create_problem.create_test_file', mock_create_test_file
            )
            create_problem_main()
            solution_exists = False
            test_exists = False
            solution_file_content = ''
            test_file_content = ''
            for file_path in (self.temp_dir / 'solutions').iterdir():
                if 'two_sum_0001.py' in file_path.name:
                    solution_exists = True
                    solution_file_content = file_path.read_text()
                    break
            for file_path in (self.temp_dir / 'tests').iterdir():
                if 'test_two_sum_0001.py' in file_path.name:
                    test_exists = True
                    test_file_content = file_path.read_text()
                    break
            assert solution_exists, "Solution file should be created"
            assert test_exists, "Test file should be created"
            assert 'class Solution:' in solution_file_content
            assert 'Description' in solution_file_content
            assert '[1,2]' in test_file_content
            assert 'from solutions.two_sum_0001 import Solution' in test_file_content
        finally:
            sys.argv = original_argv
