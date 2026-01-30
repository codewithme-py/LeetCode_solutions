# LeetCode Solutions

My clean, typed, and tested solutions to LeetCode problems (Python 3.10+).

<!-- START_STATS -->

<!-- END_STATS -->

<!-- START_TABLE -->
## Problems
| # | Title | Difficulty | Solution |
|---|-------|------------|----------|

<!-- END_TABLE -->

<hr>

<details>
<summary><b>Installation guide & description</b></summary>

Этот репозиторий — не просто сборник решений, а **готовая среда для практики LeetCode** с автоматизацией и профессиональным workflow.

### 💡 Что получает клонировавший:
- ✅ Все решения на **Python ^3.10** с type hints  
- ✅ Тесты для каждой задачи (`pytest`)  
- ✅ Автоматическая проверка стиля (`ruff`)  
- ✅ Автообновляемый `README.md` с прогрессом и ссылками  
- ✅ Готовая CI/CD-настройка через GitHub Actions  
- ✅ Чёткая структура: `solutions/`, `tests/`, `scripts/`

⚠️ Для работы скрипта обновления README требуется интернет (запрос к LeetCode 'API' при первом запуске).

⚠️ Именование файлов

Номер задачи — 4 цифры с ведущими нулями — всегда в конце имени файла, после `_`.

| Тип  | Шаблон | Обязательно? |
|------|------|-------------|
| Решение | {название_snake_case}_{NNNN}.py | Да (для парсинга номера) |
| Тест | test_{название_snake_case}_{NNNN}.py | Желательно (для ясности), но достаточно test_{название_snake_case/или номер}.py |


<hr>

<details>
<summary><i>Description (EN)</i></summary>

This repo provides a production-grade setup for LeetCode practice:
- Typed, tested Python 3.10+ solutions
- Automated README generation with progress bars
- Preconfigured CI (tests + linter) and CD (auto-update)
- No manual work — just solve, commit, PR

⚠️ For proper README generation, internet access is required (to query LeetCode 'API' on first run).

⚠️ Naming convention

The problem number — 4 digits with leading zeros — always at the end of the filename, after _.

| Type | Pattern | Required? |
|------|-------|-----------|
| Solution | {problem_name_snake_case}_{NNNN}.py | Yes (for number parsing) |
| Test | test_{problem_name_snake_case}_{NNNN}.py | Recommended (for clarity), but enough to have test_{problem_name_snake_case/or number}.py |
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
python -m venv .venv
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
#### 5. Создай токен GitHub и добавь его в Secrets репозитория
1) https://github.com/settings/tokens → перейди по ссылке
2) Generate new token (classic) → Note: `What’s this token for?` → Expiration: `your choice` → Scopes: `repo`+`workflow` → Generate token → Скопируй токен
3) Repo LeetCode_solutions Settings → Secrets and variables → Actions → New repository secret с именем `GH_PAT` → Вставь токен → Add secret

#### 6. Создавай новую feat/ветку → Решай новую задачу → делай push → PR → merge в main → CI/CD сделает всё остальное автоматически!
1) Удаление веток опционально (в истории коммитов сохраняется вся инфа)
</details>
<hr>