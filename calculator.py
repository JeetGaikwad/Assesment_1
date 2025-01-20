class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Division of Two numbers
    def div(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed")


try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    calculate = Calculator(first_number, second_number)
    print(calculate.div())
except ValueError:
    print("Invalid input. Please enter valid Input")
