class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Modulo of Two numbers
    def mod(self):
        try:
            return self.a % self.b
        except ZeroDivisionError:
            print("Error: Modulo operation with zero is not allowed.")


try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    calculate = Calculator(first_number, second_number)
    print(calculate.mod())
except:
    print("Invalid input. Please enter valid number.")
