import math

# Taking input from the user
num = float(input("Enter a number: "))

# Calculating square root, natural logarithm, and sine
square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)

# Displaying the results
print(f"\nSquare root of {num}: {square_root}")
print(f"Natural logarithm of {num}: {natural_log}")
print(f"Sine of {num} (in radians): {sine_value}")