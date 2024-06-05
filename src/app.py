from src.calculate import calculate


def main():
    try:
        x = float(input("Enter 1-st number: "))
        y = float(input("Enter 2-nd number: "))
        operator = input("Enter operation: ")
        print(f"Result: {x} {operator} {y} = {calculate(x, y, operator)}")
    except ValueError as err:
        print(f'Error: {err}')
    except KeyError:
        print(f"Error: unknown operator '{operator}'. Cannot calculate expression.")
    except ZeroDivisionError:
        print("Error: cannot divide, second operand equal 0.")

