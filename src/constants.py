# regular expressions for different types of tokens
NUMBER_RE = r"\d+(?:\.\d+)?"
OPERATIONS_RE = r"(\*\*|//|%|\*|/|\+|-)"
LBRACKET_RE = r"(\()"
RBRACKET_RE = r"(\))"
SPACE_RE = r"(\s*)"

# all available operations and their priorities
OPERATORS = ["**", "//", "%", "*", "/", "+", "-"]
RIGHT_ASSOC = {"**"}
PRECEDENCE = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '%': 2,
    '//': 2,
    '**': 3,
}
