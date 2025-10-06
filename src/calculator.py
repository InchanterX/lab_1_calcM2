from typing import List
from src.parser import Token


class Calculator:
    '''
    Подсчитывает результат выражения представленного в обратной польской нотации
    '''

    def __init__(self, tokens: List[Token]):
        self.tokens = tokens

    def count_rpn(self) -> float:
        stack=[]
        for token in self.tokens:
            if token.type == "NUMBER":
                stack.append(token.value)
            elif token.type == "OPERATIONS":
                try:
                    second_number=stack.pop()
                    first_number=stack.pop()
                except:
                    raise SyntaxError("В заданном выражении не достаточно операндов!")
                if token.value == "+":
                    stack.append(first_number+second_number)
                elif token.value == "-":
                    stack.append(first_number-second_number)
                elif token.value == "*":
                    stack.append(first_number*second_number)
                elif token.value == "/":
                    if second_number == 0:
                        raise ZeroDivisionError("Деление на ноль невозможно!")
                    stack.append(first_number/second_number)
                elif token.value == "%":
                    if isinstance(first_number, float) or isinstance(second_number, float):
                        raise TypeError("Операция % не поддерживает операция с числами с плавающей точкой!")
                    elif second_number == 0:
                        raise ZeroDivisionError("Деление на ноль невозможно!")
                    stack.append(first_number%second_number)
                elif token.value == "//":
                    if isinstance(first_number, float) or isinstance(second_number, float):
                        raise TypeError("Операция // не поддерживает операция с числами с плавающей точкой!")
                    elif second_number == 0:
                        raise ZeroDivisionError("Деление на ноль невозможно!")
                    stack.append(first_number//second_number)
                elif token.value == "**":
                    stack.append(first_number**second_number)
                # else:
                #     raise SyntaxError(f"Непредвиденный токен: {token}!")
        if len(stack)!=1:
            raise SyntaxError("Ошибка в выражении, остались не использованные значения!")
        return stack[0]