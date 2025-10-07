import pytest
from src.facade import Facade

@pytest.mark.parametrize("expression,expected", [
    ("2+3 *  4", 14.0),
    ("(2 + 3) * 4", 20.0),
    ("-5 + 2", -3.0),
    ("10 // 3", 3.0),
    ("10%3", 1.0),
    ("2 ** 3", 8),
    ("-5 --5 ++4", 4.0),
    ("-5 ---5 +++4", -6.0),
    ("-5 -+-5 +-+4", -4.0),
])

def test_facade_valid_expressions(expression,expected):
    assert Facade().calculate(expression) == expected

@pytest.mark.parametrize("expression,expected_exception,match", [
    ("10 / 0", ZeroDivisionError, "Деление на ноль невозможно!"),
    ("10 // 0", ZeroDivisionError, "Деление на ноль невозможно!"),
    ("10 % 0", ZeroDivisionError, "Деление на ноль невозможно!"),
    ("10 // 1.0", TypeError, "Операция // не поддерживает операция с числами с плавающей точкой!"),
    ("10 % 1.0", TypeError, "Операция % не поддерживает операция с числами с плавающей точкой!"),
    ("(10 +  2", SyntaxError, "Выражение содержит лишние скобки!"),
    (" 10 + 2 2", SyntaxError, "Ошибка в выражении, остались не использованные значения!")
])

def test_facade_invalid_expressions(expression,expected_exception,match):
    with pytest.raises(expected_exception, match=match):
        Facade().calculate(expression)