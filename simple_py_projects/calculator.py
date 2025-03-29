
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero is not allowed"
    else:
        return "Invalid operator"


try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Choose an operation (+, -, *, /): ")

    result = calculate(num1, num2, operator)

    print(f"Result: {result}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
