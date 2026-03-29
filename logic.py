def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, try again")


def get_operation():
    while True:
        op = input("Enter operation (+, -, *, / or =): ").strip()
        if op in ["+", "-", "*", "/", "="]:
            return op
        else:
            print("Invalid operation, try again")


def calc(a, b, opt):
    if opt == "+":
        return a + b
    elif opt == "-":
        return a - b
    elif opt == "*":
        return a * b
    elif opt == "/":
        if b == 0:
            print("Cannot divide by zero")
            return None
        return a / b
    else:
        print("Invalid operation")
        return None


if __name__ == "__main__":
    a = get_number("Enter first number: ")
    opt = get_operation()

    if opt == "=":
        print("Calculator stopped")
    else:
        b = get_number("Enter second number: ")
        result = calc(a, b, opt)

        if result is not None:
            print("Result:", result)

            while True:
                opt = get_operation()

                if opt == "=":
                    print("Final Result:", result)
                    break

                b = get_number("Enter next number: ")
                new_result = calc(result, b, opt)

                if new_result is not None:
                    result = new_result
                    print("Result:", result)