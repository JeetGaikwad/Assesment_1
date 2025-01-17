class Calculator:
    # Modulo of Two numbers
    def mod(self, a, b):
        return a % b
    
    

calculate = Calculator()
inp1 = int(input("Enter first number: "))
inp2 = int(input("Enter second number: "))
print(calculate.mod(inp1, inp2))
    