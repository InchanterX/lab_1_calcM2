


# Структура проекта

 <pre>
    .
    ├── lab_calcM2
    │   ├── src/                               # Source code
    │       ├── __init__.py                    #
    |       ├── calculator.py                  # Calculate the expression in RPN
    │       ├── constants.py                   # Constants used across the project
    │       ├── facade.py                      # Gather all the parts into one class
    │       ├── main.py                        # It is a main file!
    │       ├── parser.py                      # Convert tokens to the RPN
    │       ├── tokenizer.py                   # Tokenize the entered string
    │   ├── tests/                             # Unit tests
    │       ├── test_calculator.py             # Test calculations process
    │       ├── test_facade.py                 # Test how classes work together
    │       ├── test_parser.py                 # Test conversion to the RPN
    │       ├── test_tokenizer.py              # Tests expression tokenization
    │   ├── uv.lock                            # зависимости проекта
    │   ├── .gitignore                         # git ignore files
    │   ├── .pre-commit-config.yaml            # Code-style check
    │   ├── requirements.txt                   # Dependencies
    │   ├── README.md                          # Laboratory report with a project description
</pre>

# Assumptions
1. White spaces are insignificant
2. It is prohibited to place more than two unary operations in a row
3. All "raise"s in programme use basic error classes with specific output messages

# How it works?