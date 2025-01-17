class Calculator:
    # Exponential of Two numbers
    def exp(self, a, b):
        return a ** b
    
    

calculate = Calculator()
inp1 = int(input("Enter first number: "))
inp2 = int(input("Enter second number: "))
print(calculate.exp(inp1, inp2))
    