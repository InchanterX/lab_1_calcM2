import re
from dataclasses import dataclass
from typing import List, Any
import src.constants

@dataclass
class Token:
    type: str
    value: Any
    pos: int

class Tokenizer:
    """
    Преобразует входную строку в список токенов
    """
    def __init__(self) -> None:
        parts = [
            f"(?P<NUMBER>{src.constants.NUMBER_RE})",
            f"(?P<OPERATIONS>{src.constants.OPERATIONS_RE})",
            f"(?P<LBRACKET>{src.constants.LBRACKET_RE})",
            f"(?P<RBRACKET>{src.constants.RBRACKET_RE})",
            f"(?P<SPACE>{src.constants.SPACE_RE})",
            f"(?P<UNKNOWN>.)",
        ]
        self.master_re = re.compile("|".join(parts))

    def tokenize(self, expr: str) -> List[Token]:
        """
        Токенизирует выражение в список токенов.
        Возвращаемая последовательность не отмечает унарность, эта задача возложена на парсер.
        """
        tokens: List[Token] = []
        pos = 0
        for m in self.master_re.finditer(expr):
            kind = m.lastgroup
            text = m.group(0)
            start = m.start()
            if kind == "SPACE":
                pass
            elif kind == "NUMBER":
                value = int(text) if "." not in text else float(text)
                tokens.append(Token("NUMBER", value, start))
            elif kind == "OPERATIONS":
                tokens.append(Token("OPERATIONS",text,start))
            elif kind == "LBRACKET" or kind == "RBRACKET":
                tokens.append(Token(kind, text, start))
            elif kind == "UNKNOWN":
                raise SyntaxError(f"Неизвестный токен {text!r} на позиции {start}")
            pos = m.end()
        return tokens
