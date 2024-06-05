from src.calculate import calculate


def main():
    try:
        x = float(input("Enter 1-st number: "))
        y = float(input("Enter 2-nd number: "))
        op = input("Enter operation: ")
        print(f"Result: {x} {op} {y} = {calculate(x, y, op)}")
    except ValueError as err:
        print(f"Error: {err}")
    except KeyError:
        print(f"Error: unknown operator '{op}'. Cannot calculate expression.")
    except ZeroDivisionError:
        print("Error: cannot divide, second operand equal 0.")
