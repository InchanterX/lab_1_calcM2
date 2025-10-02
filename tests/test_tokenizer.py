from src.tokenizer import Tokenizer, Token

def test_number_and_operations():
    t = Tokenizer()
    expression="3 + 4 * 2**3 // 5"
    tokens = t.tokenize(expression)

    # Временный вывод
    print(f"\nТокенизация выражения: {expression!r}")
    for i, token in enumerate(tokens):
        print(f"Токен {i}: {token.type} = {token.value} (позиция: {token.pos})")

    assert [tok.type for tok in tokens] == ["NUMBER", "OPERATIONS", "NUMBER", "OPERATIONS", "NUMBER", "OPERATIONS", "NUMBER", "OPERATIONS", "NUMBER"]
