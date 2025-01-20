class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Multiplication of Two numbers
    def mul(self):
        return self.a * self.b


try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    calculate = Calculator(first_number, second_number)
    print(calculate.mul())
except ValueError:
    print("Invalid input. Please enter valid number")
