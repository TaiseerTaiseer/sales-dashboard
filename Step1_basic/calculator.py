print("Welcome to Taiseer's Python Calculator 🧮")

# Get user input
num1 = float(input("Enter the first number: "))
operator = input("Choose an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform calculation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator"

# Show result
print("Result:", result)
