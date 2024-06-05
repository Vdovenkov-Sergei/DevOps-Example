from src.calculate import calculate
from src.greeting import greeting


def main():
    greeting(input("What's your name? "))

    while True:
        try:
            x = float(input("Enter 1-st number: "))
            y = float(input("Enter 2-nd number: "))
            op = input("Enter operation: ")
            print(f"Result: {x} {op} {y} = {calculate(x, y, op)}\n")
        except ValueError as err:
            print(f"Error: {err}\n")
        except KeyError:
            print(f"Error: can't calculate, unknown operator '{op}'\n")
        except ZeroDivisionError:
            print("Error: can't divide, second operand equal 0.\n")

        answer = input("More? ").lower()
        if answer == "yes":
            continue
        elif answer.lower() == "no":
            break
        else:
            print("I didn't understand you, but give me another example.")
