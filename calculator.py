class Calculator:
    # Multiplication of Two numbers
    def mul(self, a, b):
        return a * b
    
    

calculate = Calculator()
inp1 = int(input("Enter first number: "))
inp2 = int(input("Enter second number: "))
print(calculate.mul(inp1, inp2))
    