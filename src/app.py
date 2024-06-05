from src.calculate import calculate


def main():
    x = int(input("Enter 1-st number: "))
    y = int(input("Enter 2-nd number: "))
    operator = input("Enter operation: ")
    print(f"Result: {x} {operator} {y} = {calculate(x, y, operator)}")
