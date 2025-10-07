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
        previous_token = None
        negate_next_number = False
        unary_operations_counter = 0

        for token in self.tokens:
            if token.type == "NUMBER":
                if negate_next_number == True:
                    token.value = -token.value
                    negate_next_number = False
                output.append(token)
                unary_operations_counter = 0
            elif token.type == "OPERATIONS":
                if token.value == "+" or token.value == "-":
                    if previous_token == None or previous_token.type == "OPERATIONS" or previous_token.type == "LBRACKET":
                        unary_operations_counter += 1
                        if unary_operations_counter > 2:
                            raise SyntaxError(
                                f"Слишком много подряд-идущих унарных операций!")
                        if token.value == "-":
                            negate_next_number = not negate_next_number
                        continue
                    else:
                        unary_operations_counter = 0

                if previous_token is None or previous_token.type == "OPERATIONS" or previous_token.type == "LBRACKET":
                    raise SyntaxError(
                        f"Лишняя операция {token.value} на позиции {token.pos}!")

                while (
                    stack != []
                    and stack[-1].type == "OPERATIONS"
                    and (
                        (stack[-1].value not in RIGHT_ASSOC and PRECEDENCE[stack[-1].value]
                         >= PRECEDENCE[token.value])
                        or (stack[-1].value in RIGHT_ASSOC and PRECEDENCE[stack[-1].value] > PRECEDENCE[token.value])
                    )
                ):
                    output.append(stack.pop())
                stack.append(token)
                unary_operations_counter = 0

            elif token.type == "LBRACKET":
                stack.append(token)
                unary_operations_counter = 0

            elif token.type == "RBRACKET":
                while stack != [] and stack[-1].type != 'LBRACKET':
                    output.append(stack.pop())
                if stack == []:
                    raise SyntaxError("Лишняя закрывающаяся скобка!")
                else:
                    stack.pop()
                unary_operations_counter = 0

            previous_token = token

        if negate_next_number == True:
            raise SyntaxError(
                "Выражение не может заканчиваться унарным оператором!")

        if previous_token is not None and previous_token.type == "OPERATIONS":
            raise SyntaxError(
                f"Выражение не может заканчиваться оператором {previous_token.value}!")

        while stack != []:
            if stack[-1].type in ("LBRACKET", "RBRACKET"):
                raise SyntaxError("Выражение содержит лишние скобки!")
            else:
                output.append(stack.pop())

        return output
