from typing import List
from src.tokenizer import Token
from src.constants import PRECEDENCE, RIGHT_ASSOC


class Parser:
    '''
    Parse the list of tokens and convert the expression
    to the RPN (Reversed Poland Notation)
    '''

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens

    def convert_to_rpm(self) -> List[Token]:
        output: List[Token] = []
        stack: List[Token] = []
        previous_token = None
        # Save the unary minus during the parsing and use it to negate the next number
        negate_next_number = False
        # Count the quantity of unary operations to prevent their excessive usage
        unary_operations_counter = 0

        for token in self.tokens:
            # Append numbers to the output, negate them if needed
            if token.type == "NUMBER":
                if negate_next_number == True:
                    token.value = -token.value
                    negate_next_number = False
                output.append(token)
                unary_operations_counter = 0
            # Append operations in RPN order
            elif token.type == "OPERATIONS":
                # Separate the unary operations,
                # make an exception if they are used wrongly
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

                # Check for excessive operations
                if previous_token is None or previous_token.type == "OPERATIONS" or previous_token.type == "LBRACKET":
                    raise SyntaxError(
                        f"Лишняя операция {token.value} на позиции {token.pos}!")

                # Switch the order of operations according to their priorities
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

            # Append opening brackets
            elif token.type == "LBRACKET":
                stack.append(token)
                unary_operations_counter = 0

            # Append closing brackets and check for errors
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

        # Finish the stack by appending left elements
        while stack != []:
            if stack[-1].type in ("LBRACKET", "RBRACKET"):
                raise SyntaxError("Выражение содержит лишние скобки!")
            else:
                output.append(stack.pop())

        return output
