import os
import platform

# Dictionary of operations
operations = {
    "+": "Addition", 
    "-": "Subtraction", 
    "*": "Multiplication", 
    "/": "Division", 
    "^": "Exponentiation"
}

def clear_terminal():
    """Clears the terminal depending on the operating system."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def choose_operation():
    """Displays available operations and returns the user's choice."""
    clear_terminal()
    i = 0
    for op, name in operations.items():
        print(i, ":", name)
        i += 1
    print("")
    print("Choose the operation you want to perform:")
    op = input()
    return list(operations.keys())[int(op)]

def perform_calculation(op, v1, v2):
    """Performs the calculation based on the chosen operation."""
    if op == '+':
        return v1 + v2
    elif op == '-':
        return v1 - v2
    elif op == '*':
        return v1 * v2
    elif op == '/':
        return v1 / v2
    elif op == '^':
        return v1 ** v2

def run_calculator():
    """Runs the main flow of the calculator."""
    while True:
        op_string = choose_operation()

        print("")
        print(">>> {} selected.".format(op_string))
        print("")
        print("What is the first number?")
        v1 = float(input())
        print("What is the second number?")
        v2 = float(input())

        result = perform_calculation(op_string, v1, v2)

        print("")
        print("{} {} {} = {}".format(v1, op_string, v2, result))
        print("")
        print("===========")
        print("Would you like to perform another operation? 0 - YES, 1 - NO")
        if float(input()) == 1:
            break

# Author: Murilo Krominski