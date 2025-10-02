from src.tokenizer import Tokenizer, Token

def test_number_and_operations():
    t = Tokenizer()
    expression="+3 + 4.25 * 2**3 // 5 + -3.00001"
    tokens = t.tokenize(expression)

    # Временный вывод
    print(f"\nТокенизация выражения: {expression!r}")
    for i, token in enumerate(tokens):
        print(f"Токен {i}: {token.type} = {token.value} (позиция: {token.pos})")

    assert [tok.type for tok in tokens] == ["OPERATIONS", "NUMBER", "OPERATIONS", "NUMBER", "OPERATIONS", "NUMBER", "OPERATIONS", "NUMBER", "OPERATIONS", "NUMBER", "OPERATIONS", "OPERATIONS", "NUMBER"]


def test_extra_spaces():
    t = Tokenizer()
    expression="3.1        + 4.2*1    //  2"
    tokens = t.tokenize(expression)

    # Временный вывод
    print(f"\nТокенизация выражения: {expression!r}")
    for i, token in enumerate(tokens):
        print(f"Токен {i}: {token.type} = {token.value} (позиция: {token.pos})")

    assert [tok.type for tok in tokens] == ["NUMBER", "OPERATIONS", "NUMBER", "OPERATIONS", "NUMBER", "OPERATIONS", "NUMBER"]

# def test_unknown_input():
#     t = Tokenizer()
#     expression="3.1 + ананас"
#     tokens = t.tokenize(expression)

#     # Временный вывод
#     print(f"\nТокенизация выражения: {expression!r}")
#     for i, token in enumerate(tokens):
#         print(f"Токен {i}: {token.type} = {token.value} (позиция: {token.pos})")

#     assert [tok.type for tok in tokens] == ["NUMBER", "OPERATIONS", "UNKNOWN"]
