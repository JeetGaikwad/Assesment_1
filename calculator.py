class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Exponential of Two numbers
    def exp(self):
        return self.a ** self.b


try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    calculate = Calculator(first_number, second_number)
    print("\nExponential: ", calculate.exp())
except ValueError:
    print("Invalid input. Please enter valid number")
