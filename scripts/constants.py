"""Constants for the LeetCode Solutions project."""


PROBLEM_NUMBER_REGEX = r'(\d+)(?=_*\.py$)'
FILENAME_SANITIZE_REGEX = r'[^a-zA-Z0-9]'

BAR_WIDTH = 10
DEFAULT_PROBLEM_ID_WIDTH = 4

BRANCH_EXISTS_MSG = 'Branch {} already exists'
CREATED_BRANCH_MSG = 'Created branch: {}'
ERROR_CREATING_BRANCH_MSG = 'Error creating branch: {}'
ERROR_CREATING_GIT_BRANCH_MSG = 'Error creating git branch: {}'
CACHED_N_PROBLEMS_MSG = 'Cached {} problems.'
GET_ALL_LEETCODE_PROBLEMS_MSG = 'Get all LeetCode problems...'
UPDATED_README_WITH_N_SOLVED_PROBLEMS_MSG = 'Updated README with {} solved problems.'
CACHE_IS_OLDER_THAN_A_WEEK_MSG = (
    'Cache is older than a week. Last update: {}. Fetching fresh data...'
)
CACHE_IS_OLDER_THAN_N_DAYS_MSG = (
    'Cache is older than {} days. Last update: {}. Fetching fresh data...'
)

GRAPHQL_URL = 'https://leetcode.com/graphql'
LEETCODE_BASE_URL = 'https://leetcode.com/problems'

CACHE_EXPIRATION_DAYS = 7

SOLUTION_FILENAME_PATTERN = '{}_{:04d}.py'
TEST_FILENAME_PATTERN = 'test_{}_{:04d}.py'

BRANCH_NAME_PATTERN = 'feat/{}-{:04d}'

FORCE_REFRESH_CACHE_HELP = 'Force refresh the problems cache from LeetCode API'
PROBLEM_ID_ARG_HELP = 'The problem ID to create'

CREATE_NEW_LEETCODE_PROBLEM_DESCRIPTION = 'Create a new LeetCode problem solution'
UPDATE_README_DESCRIPTION = 'Update README with LeetCode solutions statistics'

PROBLEM_NOT_FOUND_IN_CACHE_MSG = 'Problem with ID {} not found in cache.'
FAILED_TO_CREATE_GIT_BRANCH_MSG = 'Failed to create git branch.'

CREATED_SOLUTION_AT_MSG = 'Created solution at: {}'
CREATED_TEST_AT_MSG = 'Created test at: {}'
CREATING_SOLUTION_FOR_PROBLEM_MSG = (
    'Creating solution for Problem {}: {} (Difficulty: {})'
)
FETCHING_PROBLEM_DETAILS_MSG = 'Fetching details for problem \'{}\'...'
CACHE_OUTDATED_WARNING_MSG = (
    'Warning: Cache is outdated (missing titleSlug). Fetching empty template.'
)
CACHE_UPDATE_FAILED_MSG = 'Failed to update cache: {}. Using existing cache.'
ERROR_FETCHING_DETAILS_MSG = 'Error fetching problem details: {}'
FILE_ALREADY_EXISTS_MSG = 'File {} already exists and is not empty. Skipping creation.'
GRAPHQL_ERROR_MSG = 'GraphQL Error: {}'

CREATED_SOLUTION_FILE_MSG = 'Created solution file: {}'
CREATED_TEST_FILE_MSG = 'Created test file: {}'

GIT_CMD = 'git'
GIT_CHECKOUT_CMD = 'checkout'
GIT_BRANCH_CMD = 'branch'
GIT_LIST_FLAG = '--list'
GIT_CREATE_BRANCH_CMD = '-b'

GIT_BRANCH_PATTERN_PREFIX = r'^\s*\*?\s*'
GIT_BRANCH_PATTERN_SUFFIX = r'\s*$'
