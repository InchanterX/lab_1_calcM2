import pytest
from src.tokenizer import Tokenizer
from src.parser import Parser
from src.calculator import Calculator

def test_basic_expression():
    expression = "15 + 3"
    tokens= Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    result=Calculator(rpn).count_rpn()
    assert result == 18.0

def test_basic_operations():
    expression = "15 +   3 * 4 /  2"
    tokens= Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    result=Calculator(rpn).count_rpn()
    assert result == 21.0

def test_correct_operations_with_restrictions():
    expression = "15%3 - 2//2"
    tokens= Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    result=Calculator(rpn).count_rpn()
    assert result == -1.0

def test_powers():
    expression = "15**2-1"
    tokens= Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    result=Calculator(rpn).count_rpn()
    assert result == 224.0

def test_expressions_with_brackets():
    expression = "(15 +   3) * 4 //  2**2 + 1"
    tokens= Tokenizer().tokenize(expression)
    rpn = Parser(tokens).convert_to_rpm()
    result=Calculator(rpn).count_rpn()
    assert result == 19.0

# Нужно доделать тест для унарных операций
# def test_unary_numbers():
#     expression = "(-15 +   3) * 4 //  2**2 + 1"
#     tokens= Tokenizer().tokenize(expression)
#     rpn = Parser(tokens).convert_to_rpm()
#     result=Calculator(rpn).count_rpn()
#     assert result == 19.0