class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Subtraction of Two numbers
    def sub(self):
        return self.a - self.b

try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    calculator = Calculator(first_number, second_number)    
    print("\nSubtraction: ",calculator.sub())
except ValueError:
    print("Invalid input. Please Enter valid number")