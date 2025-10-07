import pytest
from src.tokenizer import Tokenizer
from src.parser import Parser
from src.calculator import Calculator


def test_basic_expression():
    expression = "15 + 3"
    tokens = Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    result = Calculator(rpn).count_rpn()
    assert result == 18.0


def test_basic_operations():
    expression = "15 +   3 * 4 /  2"
    tokens = Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    result = Calculator(rpn).count_rpn()
    assert result == 21.0


def test_correct_operations_with_restrictions():
    expression = "15%3 - 2//2"
    tokens = Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    result = Calculator(rpn).count_rpn()
    assert result == -1.0


def test_powers():
    expression = "15**2-1"
    tokens = Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    result = Calculator(rpn).count_rpn()
    assert result == 224.0


def test_expressions_with_brackets():
    expression = "(15 +   3) * 4 //  2**2 + 1"
    tokens = Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    result = Calculator(rpn).count_rpn()
    assert result == 19.0


def test_unary_numbers():
    expression = "(-15 +   3) * 4 //  2**2 +- 1"
    tokens = Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    result = Calculator(rpn).count_rpn()
    assert result == -13.0


def test_float_numbers():
    expression = "3,14 / 2.13"
    tokens = Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    result = Calculator(rpn).count_rpn()
    assert result == 1.4741784037558687


def test_zero_division_1():
    expression = "3,14 / 0"
    tokens = Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    with pytest.raises(ZeroDivisionError, match="Деление на ноль невозможно!"):
        Calculator(rpn).count_rpn()


def test_zero_division_2():
    expression = "3 // 0"
    tokens = Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    with pytest.raises(ZeroDivisionError, match="Деление на ноль невозможно!"):
        Calculator(rpn).count_rpn()


def test_zero_division_3():
    expression = "3 % 0"
    tokens = Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    with pytest.raises(ZeroDivisionError, match="Деление на ноль невозможно!"):
        Calculator(rpn).count_rpn()


def test_float_prohibited_operation_1():
    expression = "3.1 // 1"
    tokens = Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    with pytest.raises(TypeError, match="Операция // не поддерживает операция с числами с плавающей точкой!"):
        Calculator(rpn).count_rpn()


def test_float_prohibited_operation_2():
    expression = "3.1 % 1"
    tokens = Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    with pytest.raises(TypeError, match="Операция % не поддерживает операция с числами с плавающей точкой!"):
        Calculator(rpn).count_rpn()


def test_extra_symbols():
    expression = "3.1 * 1 2"
    tokens = Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    with pytest.raises(SyntaxError, match="Ошибка в выражении, остались не использованные значения!"):
        Calculator(rpn).count_rpn()
