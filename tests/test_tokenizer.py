import pytest
from src.tokenizer import Tokenizer, Token

def test_number_and_operations():
    t = Tokenizer()
    expression="2+2*2"
    tokens = t.tokenize(expression)
    assert [tok.type for tok in tokens] == ["NUMBER", "OPERATIONS", "NUMBER", "OPERATIONS", "NUMBER"]

def test_brackets():
    t = Tokenizer()
    expression="(2+2)*2"
    tokens = t.tokenize(expression)
    assert [tok.type for tok in tokens] == ["LBRACKET", "NUMBER", "OPERATIONS", "NUMBER", "RBRACKET", "OPERATIONS", "NUMBER"]

def test_floats():
    t = Tokenizer()
    expression="(3.14+2)*2.0001"
    tokens = t.tokenize(expression)
    assert [tok.type for tok in tokens] == ["LBRACKET", "NUMBER", "OPERATIONS", "NUMBER", "RBRACKET", "OPERATIONS", "NUMBER"]

def test_extra_spaces():
    t = Tokenizer()
    expression="3.1        + 4.2*1    //  2"
    tokens = t.tokenize(expression)
    assert [tok.type for tok in tokens] == ["NUMBER", "OPERATIONS", "NUMBER", "OPERATIONS", "NUMBER", "OPERATIONS", "NUMBER"]

def test_unknown():
    t = Tokenizer()
    expression="2-a"
    with pytest.raises(SyntaxError, match="Неизвестный токен 'a' на позиции 2"):
        tokens = t.tokenize(expression)

def test_potentially_incorrect_expression():
    t = Tokenizer()
    expression="2*-2-"
    tokens = t.tokenize(expression)
    assert [tok.type for tok in tokens] == ["NUMBER", "OPERATIONS", "OPERATIONS", "NUMBER", "OPERATIONS"]