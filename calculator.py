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

    # Multiplication of Two numbers
    def mul(self):
        return self.a * self.b

    # Addition of Two numbers
    def add(self):
        return self.a + self.b

    # Subtraction of Two numbers
    def sub(self):
        return self.a - self.b


try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    calculator = Calculator(first_number, second_number)
    print("\nSubtraction: ", calculator.sub())
    print("Addition: ", calculator.add())
    print("Multiplication: ", calculator.mul())
    print("Division: ", calculator.div())
except ValueError:
    print("Invalid input. Please Enter valid number")
