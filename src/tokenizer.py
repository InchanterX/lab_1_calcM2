import re
from dataclasses import dataclass
from typing import List, Any
import src.constants


@dataclass
class Token:
    '''
    Class for token contains three parts
    - type of the token
    - value contained in token
    - original position of token in the entered string
    '''
    type: str
    value: Any
    pos: int


class Tokenizer:
    """
    Tokenize the entered string by creating a list of tokens
    splitted by the regular expressions.
    """

    # Define all needed variables
    def __init__(self) -> None:
        '''
        Gather all the regular expressions and
        merge all the tokens' regular expressions into one splitted by |
        '''
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
        Tokenize the expression into tokens.
        Tokenized list separate the unary operations as basic operations.
        They will be splitted letter.
        """
        expr = expr.replace(',', '.')
        tokens: List[Token] = []
        pos = 0
        for m in self.master_re.finditer(expr):
            kind = m.lastgroup
            text = m.group(0)
            start = m.start()
            # Skip the spaces in the expression as insignificant
            if kind == "SPACE":
                pass
            elif kind == "NUMBER":
                value = int(text) if "." not in text else float(text)
                tokens.append(Token("NUMBER", value, start))
            elif kind == "OPERATIONS":
                tokens.append(Token("OPERATIONS", text, start))
            elif kind == "LBRACKET" or kind == "RBRACKET":
                tokens.append(Token(kind, text, start))
            # Define all other symbols as unknown and raise an error
            elif kind == "UNKNOWN":
                raise SyntaxError(
                    f"Неизвестный токен {text!r} на позиции {start}")
            pos = m.end()
        return tokens
