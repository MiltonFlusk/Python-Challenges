def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1/n2


def calculator(n1, operation_selection, n2):

    operation = {
        "+": add(n1, n2),
        "-": subtract(n1, n2),
        "*": multiply(n1, n2),
        "/": divide(n1, n2)
    }
    x = operation[operation_selection]
    print(f"{n1} {operation_selection} {n2} = {x}")
    continue_calculating = input(
        f"type 'y' to continue calculating with '{x}' or 'n' to start a new calculation. ")

    if continue_calculating == "y":
        calculator(x, input("Pick an operation: "),
                   float(input("What is the next number? ")))
    elif continue_calculating == "n":
        print("\n" * 100)
        calculator(float(input("What is the first number? ")), input("Pick an operation: "),
                   float(input("What is the next number? ")))
    else:
        return


calculator(float(input("What is the first number? ")), input(
    "Pick an operation: "), float(input("What is the next number? ")))
