# Taking input from the user
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

# Performing basic mathematical operations
addition = int(num1 + num2)
subtraction = int(num1 - num2)
multiplication = int(num1 * num2)

division = float(num1 / num2) if num2 != 0 else "Undefined (cannot divide by zero)"

# Displaying the results
print("\nResults:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
