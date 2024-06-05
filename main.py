func = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


def calculate(x, y, operator):
    return func[operator](x, y)


def main():
    x = int(input("Enter 1-st number: "))
    y = int(input("Enter 2-nd number: "))
    operator = input("Enter operation: ")
    print(f"Result: {x} {operator} {y} = {calculate(x, y, operator)}")


if __name__ == "__main__":
    main()
