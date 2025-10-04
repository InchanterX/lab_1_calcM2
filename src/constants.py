NUMBER_RE = r"\d+(?:\.\d+)?"
OPERATORS = ["**", "//", "%", "*", "/", "+", "-"]
OPERATIONS_RE = r"(\*\*|//|%|\*|/|\+|-)"
LBRACKET_RE = r"(\()"
RBRACKET_RE = r"(\))"
SPACE_RE = r"(\s*)"
PRECEDENCE = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '%': 2,
    '//': 2,
    '**': 3,
}
RIGHT_ASSOC = {"**"}