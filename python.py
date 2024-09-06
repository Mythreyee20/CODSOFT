# Simple Calculator

# Function to perform calculation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

# Input: Get numbers and operation from the user
def get_user_input():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        
        # Perform calculation and display result
        result = calculate(num1, num2, operation)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

# Run the calculator
get_user_input()
