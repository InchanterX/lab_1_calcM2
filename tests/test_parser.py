import pytest
from src.tokenizer import Tokenizer
from src.parser import Parser

def test_basic_expression():
    expression = "15 + 3"
    tokens = Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    values = [token.value for token in rpn]

    # Дополнительный вывод
    print(f"\nПреобразование в польскую запись выражения: {expression!r}")
    for num, token in enumerate(tokens):
        print(f"Токен {num}: {token.type} = {token.value} (позиция: {token.pos})")
    print(f"Итоговое выражение: {values}")

    assert values == [15, 3, "+"]


def test_priorities_of_basic_expressions():
    expression = "15 * 3 + 3 / 23 - 2 % 4 // 2"
    tokens = Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    values = [token.value for token in rpn]

    # Дополнительный вывод
    print(f"\nПреобразование в польскую запись выражения: {expression!r}")
    for num, token in enumerate(tokens):
        print(f"Токен {num}: {token.type} = {token.value} (позиция: {token.pos})")
    print(f"Итоговое выражение: {values}")

    assert values == [15, 3, "*", 3, 23, "/", "+", 2, 4, "%", 2, "//", "-"]


def test_priorities_of_powers():
    expression = "15 ** 3 + 3 / 23 - 2**2 % 4 // 2**2"
    tokens = Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    values = [token.value for token in rpn]

    # Дополнительный вывод
    print(f"\nПреобразование в польскую запись выражения: {expression!r}")
    for num, token in enumerate(tokens):
        print(f"Токен {num}: {token.type} = {token.value} (позиция: {token.pos})")
    print(f"Итоговое выражение: {values}")

    assert values == [15, 3, "**", 3, 23, "/", "+", 2, 2, "**", 4, "%", 2, 2, "**", "//", "-"]

def test_brackets():
    expression = "(15 + 2) ** 3 * (2 + 3)"
    tokens = Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    values = [token.value for token in rpn]

    # Дополнительный вывод
    print(f"\nПреобразование в польскую запись выражения: {expression!r}")
    for num, token in enumerate(tokens):
        print(f"Токен {num}: {token.type} = {token.value} (позиция: {token.pos})")
    print(f"Итоговое выражение: {values}")

    assert values == [15, 2, "+", 3, "**", 2, 3, "+", "*"]


def test_floats():
    expression = "(15.2 + 2) ** 3.3 * (2.0001 + 3)"
    tokens = Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    values = [token.value for token in rpn]

    # Дополнительный вывод
    print(f"\nПреобразование в польскую запись выражения: {expression!r}")
    for num, token in enumerate(tokens):
        print(f"Токен {num}: {token.type} = {token.value} (позиция: {token.pos})")
    print(f"Итоговое выражение: {values}")

    assert values == [15.2, 2, "+", 3.3, "**", 2.0001, 3, "+", "*"]

def test_unary_operations():
    expression = "-15.2 + (-5)**+2 +-2"
    tokens = Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    values = [token.value for token in rpn]

    # Дополнительный вывод
    print(f"\nПреобразование в польскую запись выражения: {expression!r}")
    for num, token in enumerate(tokens):
        print(f"Токен {num}: {token.type} = {token.value} (позиция: {token.pos})")
    print(f"Итоговое выражение: {values}")

    assert values == [-15.2, -5, 2, "**", "+", -2, "+"]

def test_extra_operations():
    expression = "(15.2 + 5"
    tokens = Tokenizer().tokenize(expression)
    parser=Parser(tokens)
    with pytest.raises(SyntaxError):
        parser.convert_to_rpm()

def test_unclosed_brackets():
    expression = "(15.2 + 5"
    tokens = Tokenizer().tokenize(expression)
    parser=Parser(tokens)
    with pytest.raises(SyntaxError):
        parser.convert_to_rpm()

def test_extra_brackets():
    expression = "(15.2 + 5))"
    tokens = Tokenizer().tokenize(expression)
    parser=Parser(tokens)
    with pytest.raises(SyntaxError):
        parser.convert_to_rpm()