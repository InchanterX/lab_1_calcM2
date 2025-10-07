from src.tokenizer import Tokenizer
from src.parser import Parser
from src.calculator import Calculator

class Facade:
    '''
    '''

    def calculate(self, expression: str) -> float:
        tokens= Tokenizer().tokenize(expression)
        rpn = Parser(tokens).convert_to_rpm()
        result=Calculator(rpn).count_rpn()
        return result