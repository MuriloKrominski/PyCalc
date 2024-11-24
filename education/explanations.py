
def explain_calculation(operation, *args):
    if operation == "add":
        return f"Add {args[0]} and {args[1]} to get {args[0] + args[1]}."
    elif operation == "subtract":
        return f"Subtract {args[1]} from {args[0]} to get {args[0] - args[1]}."
