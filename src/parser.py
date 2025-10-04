from typing import List
from src.tokenizer import Token
from src.constants import PRECEDENCE, RIGHT_ASSOC

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens

    def convert_to_rpm(self) -> List[Token]:
        '''
        Преобразует данный список токенов в обратную польскую запись
        '''
        output: List[Token] = []
        stack: List[Token] = []

        for token in self.tokens:
            if token.type == "NUMBER":
                output.append(token)
            elif token.type == "OPERATIONS":
                while (
                    stack != []
                    and stack[-1].type == "OPERATIONS"
                    and (
                        (stack[-1].value not in RIGHT_ASSOC and PRECEDENCE[stack[-1].value] >= PRECEDENCE[token.value])
                        or (stack[-1].value in RIGHT_ASSOC and PRECEDENCE[stack[-1].value] > PRECEDENCE[token.value])
                    )
                ):
                    output.append(stack.pop())
                stack.append(token)

            elif token.type == "LBRACKET":
                stack.append(token)

            elif token.type == "RBRACKET":
                while stack != [] and stack[-1].type != 'LBRACKET':
                    output.append(stack.pop())
                if stack == []:
                    raise SyntaxError('Лишняя закрывающаяся скобка!')
                else:
                    stack.pop()

        while stack!=[]:
            if stack[-1].type in ("LBRACKET", "RBRACKET"):
                raise SyntaxError("Выражение содержит лишние скобки")
            else:
                output.append(stack.pop())

        return output