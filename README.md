


# Структура проекта

 <pre>
    .
    ├── lab_calcM2
    │   ├── src/                               # Исходный код
    │       ├── __init__.py
    |       ├── calculator.py
    │       ├── constants.py
    │       ├── facade.py
    │       ├── main.py
    │       ├── parser.py
    │       ├── tokenizer.py
    │   ├── tests/                             # Unit тесты
    │       ├── test_calculator.py
    │       ├── test_evaluate.py
    │       ├── test_parser.py
    │       ├── test_tokenizer.py
    │   ├── uv.lock                            # зависимости проекта
    │   ├── report.pdf                         # Отчет
    │   ├── .gitignore                         # git ignore файл
    │   ├── .pre-commit-config.yaml            # Средства автоматизации проверки кодстайла
    │   ├── requirements.txt                   # Зависимости
    │   ├── README.md                          # Описание проекта, с описанием файлов и с титульником о том,
                                               # что и какая задача
</pre>

# Assumptions
1. White spaces are insignificant
2. It is prohibited to place more than two unary operations in a row