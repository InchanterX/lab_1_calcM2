from typing import List
from src.parser import Token


class Calculator:
    '''
    Calculate the result for RPN
    '''

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens

    def count_rpn(self) -> float:
        stack = []
        for token in self.tokens:
            # Put the numbers to the stack
            if token.type == "NUMBER":
                stack.append(token.value)
            # Take two last elements of stack and apply operation to it
            elif token.type == "OPERATIONS":
                # Check if if is enough of elements in stack to apply operation
                try:
                    second_number = stack.pop()
                    first_number = stack.pop()
                except IndexError:
                    raise SyntaxError(
                        "В заданном выражении не достаточно операндов!")
                '''
                Apply operation depended on current and append it to the stack.
                Raise a error for attempts of zero division with /, // and %.
                Raise a error for attempts of applying // or % to a float number.
                '''
                try:
                    if token.value == "+":
                        stack.append(first_number+second_number)
                    elif token.value == "-":
                        stack.append(first_number-second_number)
                    elif token.value == "*":
                        try:
                            result = first_number*second_number
                            if len(str(result)) > 4300:
                                raise ValueError(
                                    "Результат выражения слишком велик!")
                            stack.append(result)
                        except OverflowError:
                            raise ValueError(
                                "Результат выражения слишком велик!")
                    elif token.value == "/":
                        if second_number == 0:
                            raise ZeroDivisionError(
                                "Деление на ноль невозможно!")
                        stack.append(first_number/second_number)
                    elif token.value == "%":
                        if isinstance(first_number, float) or isinstance(second_number, float):
                            raise TypeError(
                                "Операция % не поддерживает операция с числами с плавающей точкой!")
                        elif second_number == 0:
                            raise ZeroDivisionError(
                                "Деление на ноль невозможно!")
                        stack.append(first_number % second_number)
                    elif token.value == "//":
                        if isinstance(first_number, float) or isinstance(second_number, float):
                            raise TypeError(
                                "Операция // не поддерживает операция с числами с плавающей точкой!")
                        elif second_number == 0:
                            raise ZeroDivisionError(
                                "Деление на ноль невозможно!")
                        stack.append(first_number//second_number)
                    elif token.value == "**":
                        try:
                            result = first_number**second_number
                            if len(str(result)) > 4300:
                                raise ValueError(
                                    "Результат выражения слишком велик!")
                            stack.append(result)
                        except OverflowError:
                            raise ValueError(
                                "Результат выражения слишком велик!")
                    else:
                        raise SyntaxError(f"Непредвиденный токен: {token}!")
                except OverflowError:
                    raise OverflowError(
                        "Результат слишком большой для вычисления!")
                except ValueError:
                    raise OverflowError(
                        "Результат не может быть представлен числом!")
        # Return the result - one float number. If stack contains more than one element raise a error
        if len(stack) != 1:
            raise SyntaxError(
                "Ошибка в выражении, остались не использованные значения!")
        return stack[0]
