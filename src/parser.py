from typing import List
from src.tokenizer import Token
from constants import PRECEDENCE, RIGHT_ASSOC

class Parser:
    def __init__(self, tokens: List[Token]):
        self.token = tokens

    def convert_to_rpm(self) -> List[Token]:
        '''
        Преобразует данный список токенов в обратную польскую запись
        '''
        output: List[Token] = []
        stack: List[Token] = []

        for token in self.tokens:
            if token.kind == "NUMBER":
                output.append(token)
            elif token.kind == "OPERATIONS":
                while (
                    stack != []
                    and stack[-1].kind == "OPERATIONS"
                    and (
                        (stack[-1].value not in RIGHT_ASSOC and PRECEDENCE[stack[-1].value] >= PRECEDENCE[token.value])
                        or (stack[-1].value in RIGHT_ASSOC and PRECEDENCE[stack[-1].value] > PRECEDENCE[token.value])
                    )
                ):
                    output.append(stack.pop())
                stack.append(token)

            elif token.kind == "LBRAKET":
                stack.append(token)

            elif token.kind == "RBRACKET":
                while stack != [] and stack[-1].kind != 'LBRECKET':
                    output.append(stack.pop())
                if stack == []:
                    raise SyntaxError('Лишняя закрывающаяся скобка!')
                else:
                    stack.pop()

        while stack!=[]:
            if stack[-1].kind in ("LBRAKET", "RBRACKET"):
                raise SyntaxError("Выражение содержит лишние скобки")
            else:
                output.append(stack.pop())

        return output