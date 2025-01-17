class Calculator:
    # Subtraction of Two numbers
    def sub(self, a, b):
        return a - b
    # Multiplication of Two numbers
    def mul(self, a, b):
        return a * b
    # Division of Two numbers
    def div(self, a, b):
        return a / b
    # Modulo of Two numbers
    def mod(self, a, b):
        return a % b
    # Exponential of Two numbers
    def exp(self, a, b):
        return a ** b
    
    

calculate = Calculator()
inp1 = int(input("Enter first number: "))
inp2 = int(input("Enter second number: "))
print(calculate.sub(inp1, inp2))
print(calculate.mul(inp1, inp2))
print(calculate.div(inp1, inp2))
print(calculate.mod(inp1, inp2))
print(calculate.exp(inp1, inp2))
    