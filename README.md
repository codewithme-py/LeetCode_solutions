# LeetCode Solutions

My clean, typed, and tested solutions to LeetCode problems (Python 3.10+).

<!-- START_STATS -->
✅ **Total**: **10**  
🟢 **Easy**: 5 &nbsp; `░░░░░░░░░░` &nbsp; _(0.5%)_  
🟡 **Medium**: 4 &nbsp; `░░░░░░░░░░` &nbsp; _(0.2%)_  
🔴 **Hard**: 1 &nbsp; `░░░░░░░░░░` &nbsp; _(0.1%)_
<!-- END_STATS -->

<!-- START_TABLE -->
<details>
<summary><b> Show all solved problems </b></summary>

## Problems

| # | Title | Difficulty | Solution |
|---|-------|------------|----------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | [`two_sum_0001.py`](solutions/two_sum_0001.py) |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | [`add_two_numbers_0002.py`](solutions/add_two_numbers_0002.py) |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | [`longest_substring_without_repeating_characters_0003.py`](solutions/longest_substring_without_repeating_characters_0003.py) |
| 4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | [`median_of_two_sorted_arrays_0004.py`](solutions/median_of_two_sorted_arrays_0004.py) |
| 5 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Medium | [`longest_palindromic_substring_0005.py`](solutions/longest_palindromic_substring_0005.py) |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Easy | [`palindrome_number_0009.py`](solutions/palindrome_number_0009.py) |
| 12 | [Integer to Roman](https://leetcode.com/problems/integer-to-roman/) | Medium | [`integer_to_roman_0012.py`](solutions/integer_to_roman_0012.py) |
| 13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | Easy | [`roman_to_integer_0013.py`](solutions/roman_to_integer_0013.py) |
| 14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | Easy | [`longest_common_prefix_0014.py`](solutions/longest_common_prefix_0014.py) |
| 83 | [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | Easy | [`remove_duplicates_from_sorted_list_0083.py`](solutions/remove_duplicates_from_sorted_list_0083.py) |
</details>
<!-- END_TABLE -->

<hr>

<details>
<summary><b>Installation guide & description</b></summary>

Этот репозиторий — не просто сборник решений, а **готовая среда для практики LeetCode** с автоматизацией и профессиональным workflow.

### 💡 Что получает клонировавший:
- ✅ Все решения на **Python ^3.10** с type hints
- ✅ Пре-коммит-хук для запуска тестов (`pytest`) & (`ruff`)
- ✅ Автоматическое создание /feat ветки, файлов проблемы и теста
- ✅ Генерация файлов с контентом: условие задачи, сниппеты кода и примеры тестов (fetch from LeetCode API)
- ✅ Автообновляемый `README.md` с прогрессом и ссылками
- ✅ Интеллектуальное управление кэшем: автоматическое обновление раз в неделю или по требованию
- ✅ Готовая CI/CD-настройка через GitHub Actions
- ✅ Чёткая структура: `solutions/`, `tests/`, `scripts/`

⚠️ Для работы скрипта обновления README требуется интернет (запрос к LeetCode 'API' при первом запуске).

<hr>

<details>
<summary><i>Description (EN)</i></summary>

This repo provides a production-grade setup for LeetCode practice:
- Typed, tested Python 3.10+ solutions
- Pre-commit hook for running tests (`pytest`) & (`ruff`)
- Automated README generation with progress bars
- Automated creation of /feat branch, problem and test files
- Automated generation of files with content: problem statement, code snippets, and test examples (fetch from LeetCode API)
- Smart cache management: automatic weekly refresh or on-demand
- Preconfigured CI and CD (auto-update)
- No manual work — just solve, commit, PR

⚠️ For proper README generation, internet access is required (to query LeetCode 'API' on first run).

</details>

<hr>

### 🛠 Установка

#### 1. Клонируй репо
```bash
git clone https://github.com/codewithme-py/LeetCode_solutions.git
```
```bash
cd LeetCode_solutions
```

#### 2. Создай и активируй виртуальное окружение
```bash
python3 -m venv .venv
```
Linux/Mac
```bash
source .venv/bin/activate
```
или на Windows
```bash
source .venv\Scripts\activate
```

#### 3. Установи зависимости
```bash
pip install -e .[dev]
```

#### 4. Запусти тесты (проверь, что всё работает)
```bash
pytest && ruff check .
```

#### 5. Используй скрипт обновления README (опционально)
```bash
python3 scripts/update_readme.py
```
Для принудительного обновления кэша задач используйте флаг `--force-refresh-cache`:
```bash
python3 scripts/update_readme.py --force-refresh-cache
```

- Кэш задач обновляется автоматически раз в неделю (от даты изменения файла problems_cache.json). Для принудительного обновления кэша задач используйте флаг --force-refresh-cache:

#### 6. Создай токен GitHub и добавь его в Secrets репозитория
1) https://github.com/settings/tokens → перейди по ссылке
2) Generate new token (classic) → Note: `What’s this token for?` → Expiration: `your choice` → Scopes: `repo`+`workflow` → Generate token → Скопируй токен
3) Repo LeetCode_solutions Settings → Secrets and variables → Actions → New repository secret с именем `GH_PAT` → Вставь токен → Add secret

#### 7. Используй скрипт → Решай новую задачу → делай push → PR → merge в main → CI/CD сделает всё остальное автоматически!

```bash
make problem <номер_задачи>
```

1) Скрипт создает новую **/feat** ветку, а так же файлы решения и тестов минимизируя рутину
2) Удаление веток после **merge** опционально (в истории коммитов сохраняется вся инфа)
</details>
<hr>