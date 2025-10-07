from src.tokenizer import Tokenizer
from src.parser import Parser
from src.calculator import Calculator


class Facade:
    '''
    Gather all the parts of the calculator and unite them from simpler usage in the future
    '''

    def calculate(self, expression: str) -> float:
        tokens = Tokenizer().tokenize(expression)
        rpn = Parser(tokens).convert_to_rpm()
        result = Calculator(rpn).count_rpn()
        return result
