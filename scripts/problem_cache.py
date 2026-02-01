"""
Module for handling problem cache operations.

This module provides functionality to:
- Fetch LeetCode problems from the GraphQL API
- Cache problems locally to avoid repeated API calls
- Manage cache expiration and updates
"""
import datetime
import json
from pathlib import Path

import requests
from constants import (
    CACHE_IS_OLDER_THAN_A_WEEK_MSG,
    CACHE_UPDATE_FAILED_MSG,
    CACHED_N_PROBLEMS_MSG,
    GET_ALL_LEETCODE_PROBLEMS_MSG,
    GRAPHQL_URL,
)

PROJECT_ROOT = Path(__file__).parent.parent
CACHE_FILE = PROJECT_ROOT / 'problems_cache.json'


def fetch_full_problems_cache() -> dict[str, tuple[str, str, str]]:
    """
    Fetch ALL problems from LeetCode and save to cache.

    Returns:
        Dictionary mapping problem IDs to (title, difficulty, titleSlug) tuples
    """
    print(GET_ALL_LEETCODE_PROBLEMS_MSG)
    all_questions = []
    skip = 0
    limit = 100
    while True:
        query = '''
        query problemsetQuestionList($skip: Int!, $limit: Int!) {
          problemsetQuestionList: questionList(
            categorySlug: ""
            limit: $limit
            skip: $skip
            filters: {}
          ) {
            total: totalNum
            questions: data {
              questionId
              title
              difficulty
              titleSlug
            }
          }
        }
        '''
        resp = requests.post(
            GRAPHQL_URL,
            json={'query': query, 'variables': {'skip': skip, 'limit': limit}}
        )
        resp.raise_for_status()
        data = resp.json()['data']['problemsetQuestionList']
        questions = data['questions']
        total = data['total']
        if not questions:
            break
        all_questions.extend(questions)
        skip += limit
        if skip >= total:
            break
    cache = {}
    for q in all_questions:
        try:
            num = str(int(q['questionId']))
            cache[num] = (q['title'], q['difficulty'], q['titleSlug'])
        except (ValueError, KeyError, TypeError):
            continue
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=2)
    print(CACHED_N_PROBLEMS_MSG.format(len(cache)))
    return cache


def fetch_problem_data(title_slug: str) -> dict:
    """
    Fetch problem details (content, code snippets, test cases) from LeetCode.

    Args:
        title_slug: The title slug of the problem (e.g., 'two-sum')

    Returns:
        Dictionary containing problem data
    """
    query = '''
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            content
            codeSnippets {
                langSlug
                code
            }
            exampleTestcases
        }
    }
    '''
    response = requests.post(
        GRAPHQL_URL,
        json={'query': query, 'variables': {'titleSlug': title_slug}},
        timeout=10
    )
    response.raise_for_status()
    data = response.json()
    if 'errors' in data:
        raise ValueError(f'GraphQL Error: {data["errors"]}')
    return data['data']['question']


def load_problems_cache() -> dict[str, tuple[str, str, str]]:
    """
    Load cache or create new (full).

    Returns:
        Dictionary mapping problem IDs to (title, difficulty, titleSlug) tuples
    """
    if CACHE_FILE.exists():
        cache_modified_time = datetime.datetime.fromtimestamp(
            CACHE_FILE.stat().st_mtime
        )
        week_ago = datetime.datetime.now() - datetime.timedelta(weeks=1)
        if cache_modified_time < week_ago:
            print(
                CACHE_IS_OLDER_THAN_A_WEEK_MSG.format(cache_modified_time)
            )
            try:
                return fetch_full_problems_cache()
            except Exception as e:
                print(CACHE_UPDATE_FAILED_MSG.format(e))
                with open(CACHE_FILE) as f:
                    return json.load(f)
        with open(CACHE_FILE) as f:
            return json.load(f)
    return fetch_full_problems_cache()
