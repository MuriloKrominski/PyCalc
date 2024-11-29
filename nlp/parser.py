
import re

def parse_natural_language(expression):
    expression = expression.lower()
    expression = re.sub(r"plus", "+", expression)
    expression = re.sub(r"minus", "-", expression)
    expression = re.sub(r"times", "*", expression)
    expression = re.sub(r"divided by", "/", expression)
    return expression
