class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Addition of Two numbers
    def add(self):
        return self.a + self.b

    # Subtraction of Two numbers
    def sub(self):
        return self.a - self.b

    # Multiplication of Two numbers
    def mul(self):
        return self.a * self.b

    # Division of Two numbers
    def div(self):
        try:
            return self.a / self.b
        except:
            print("Error: Division by zero is not allowed.")

    # Modulo of Two numbers
    def mod(self):
        try:
            return self.a % self.b
        except:
            print("Error: Modulo operation of zero is not allowed.")

    # Exponential of Two numbers
    def exp(self):
        return self.a ** self.b


try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    calculator = Calculator(first_number, second_number)

    print("\nAddition: ", calculator.add())
    print("Subtraction: ", calculator.sub())
    print("Multiplication: ", calculator.mul())
    print("Division: ", calculator.div())
    print("Modulo: ", calculator.mod())
    print("Exponential: ", calculator.exp(), "\n")

except ValueError:
    print("Invalid input. Please Enter valid number")
