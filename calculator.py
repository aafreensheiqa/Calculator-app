def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: divide by zero"

while True:
    op = input("Enter operator (+, -, *, /) or 'q' to quit: ")
    if op == "q":
        break
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    if op == "+":
        print(add(num1, num2))
    elif op == "-":
        print(subtract(num1, num2))
    elif op == "*":
        print(multiply(num1, num2))
    elif op == "/":
        print(divide(num1, num2))
    else:
        print("Invalid operator")