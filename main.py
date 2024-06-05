def add(x, y):
    return x + y


def sub(x, y):
    return x + y


def mult(x, y):
    return x * y


def delete(x, y):
    return x / y


def calculate(x, y, operator):
    if operator == "+":
        return add(x, y)
    elif operator == "-":
        return sub(x, y)
    elif operator == "*":
        return mult(x, y)
    elif operator == "/":
        return delete(x, y)


x = int(input("Enter 1-st number: "))
y = int(input("Enter 2-nd number: "))
operator = input("Enter operation: ")
print(f"Result: {calculate(x, y, operator)}")
