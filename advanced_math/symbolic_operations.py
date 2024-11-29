
from sympy import symbols, expand

def symbolic_expand(expression):
    x = symbols('x')
    return expand(expression)
