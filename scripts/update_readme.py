# ruff: noqa: E501, UP015
#!/usr/bin/env python3
import json
import re
from collections import Counter
from pathlib import Path

import requests

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
CACHE_FILE = PROJECT_ROOT / 'problems_cache.json'
GRAPHQL_URL = 'https://leetcode.com/graphql'
LEETCODE_BASE_URL = 'https://leetcode.com/problems'


def fetch_full_problems_cache():
    """Забирает ВСЕ задачи с LeetCode постранично и сохраняет в кэш."""
    print('Get all LeetCode problems...')
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
            num = int(q['questionId'])
            cache[num] = (q['title'], q['difficulty'])
        except (ValueError, KeyError, TypeError):
            continue
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache, f, indent=2)
    print(f'Cached {len(cache)} problems.')
    return cache


def load_problems_cache():
    """Загружает кэш или создаёт новый (полный)."""
    if CACHE_FILE.exists():
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    return fetch_full_problems_cache()


def extract_problem_number(file_name: str) -> int | None:
    """Извлекает номер задачи из имени файла."""
    if not file_name.endswith('.py'):
        return None
    match = re.search(r'(\d+)(?=_*\.py$)', file_name)
    if match:
        return int(match.group(1))
    return None


def make_bar(value: int, max_val: int, width: int = 10) -> str:
    """Генерирует текстовый прогресс-бар из эмодзи."""
    if max_val == 0:
        filled = 0
    else:
        filled = min(width, max(0, int((value / max_val) * width)))
    return '█' * filled + '░' * (width - filled)


def main():
    solutions_dir = PROJECT_ROOT / 'solutions'
    readme_path = PROJECT_ROOT / 'README.md'
    problems = load_problems_cache()

    solved_files = []
    solved_stats = {'Easy': 0, 'Medium': 0, 'Hard': 0}
    if solutions_dir.exists():
        for f in solutions_dir.iterdir():
            if f.is_file():
                num = extract_problem_number(f.name)
                if num and str(num) in problems:
                    title, difficulty = problems[str(num)]
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

    easy_pct = (solved_stats['Easy'] / total_stats['Easy'] * 100) if total_stats['Easy'] else 0
    medium_pct = (solved_stats['Medium'] / total_stats['Medium'] * 100) if total_stats['Medium'] else 0
    hard_pct = (solved_stats['Hard'] / total_stats['Hard'] * 100) if total_stats['Hard'] else 0

    stats_md = (
        f'✅ **Total**: **{total_solved}**  \n'
        f'🟢 **Easy**: {solved_stats["Easy"]} &nbsp; `{easy_bar}` &nbsp; _({easy_pct:.1f}%)_  \n'
        f'🟡 **Medium**: {solved_stats["Medium"]} &nbsp; `{medium_bar}` &nbsp; _({medium_pct:.1f}%)_  \n'
        f'🔴 **Hard**: {solved_stats["Hard"]} &nbsp; `{hard_bar}` &nbsp; _({hard_pct:.1f}%)_'
    )

    if solved_files:
        table_rows = []
        for num, title, difficulty, file_name in solved_files:
            leetcode_url = f'{LEETCODE_BASE_URL}/{title.lower().replace(" ", "-")}/'
            table_rows.append(
                f'| {num} | [{title}]({leetcode_url}) | {difficulty} | [`{file_name}`](solutions/{file_name}) |'
            )
        table_md = '\n'.join(table_rows)
    else:
        table_md = '| — | — | — | — |'

    table_with_details = (
        f'<details>\n<summary><b> Show all solved problems ({total_solved})</b></summary>\n'
        '## Problems\n\n'
        '| # | Title | Difficulty | Solution |\n'
        '|---|-------|------------|----------|\n'
        f'{table_md}\n'
        '</details>'
    )

    with open(readme_path, 'r') as f:
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
    print(f'Updated README with {total_solved} solved problems.')


if __name__ == '__main__':
    main()
