# flake8: noqa
# !/usr/bin/env python3
import json
import re
from pathlib import Path
import requests

CACHE_FILE = 'problems_cache.json'
GRAPHQL_URL = 'https://leetcode.com/graphql'


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
    if Path(CACHE_FILE).exists():
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


def main():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    solutions_dir = project_root / 'solutions'
    readme_path = project_root / 'README.md'
    problems = load_problems_cache()
    solved_files = []
    stats = {'Easy': 0, 'Medium': 0, 'Hard': 0}
    if solutions_dir.exists():
        for f in solutions_dir.iterdir():
            if f.is_file():
                num = extract_problem_number(f.name)
                if num and str(num) in problems:
                    title, difficulty = problems[str(num)]
                    solved_files.append((num, title, difficulty, f.name))
                    stats[difficulty] += 1
    solved_files.sort(key=lambda x: x[0])
    total = sum(stats.values())
    if solved_files:
        table_rows = []
        for num, title, difficulty, file_name in solved_files:
            leetcode_url = f'https://leetcode.com/problems/{title.lower().replace(" ", "-")}/'
            table_rows.append(
                f'| {num} | [{title}]({leetcode_url}) | {difficulty} | [`{file_name}`](solutions/{file_name}) |'
            )
        table_md = '\n'.join(table_rows)
    else:
        table_md = '| — | — | — | — |'
    stats_md = (
        f'- ✅ Solved: {total}\n'
        f'- 🟢 Easy: {stats["Easy"]}\n'
        f'- 🟡 Medium: {stats["Medium"]}\n'
        f'- 🔴 Hard: {stats["Hard"]}'
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
        f'<!-- START_TABLE -->\n## Problems\n| # | Title | Difficulty | Solution |\n|---|-------|------------|----------|\n{table_md}\n<!-- END_TABLE -->',
        content,
        flags=re.DOTALL
    )
    with open(readme_path, 'w') as f:
        f.write(content)
    print(f'Updated README with {total} solved problems.')


if __name__ == '__main__':
    main()
