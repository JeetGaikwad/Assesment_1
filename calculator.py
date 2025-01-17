class Calculator:
    # Division of Two numbers
    def div(self, a, b):
        return a / b
    
    

calculate = Calculator()
inp1 = int(input("Enter first number: "))
inp2 = int(input("Enter second number: "))
print(calculate.div(inp1, inp2))
    