# Simple calculator with basic arithmetic operations

def calculate(a, b, op):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/": return None if b == 0 else a / b
    