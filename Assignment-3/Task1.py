def factorial(n):
    """Calculate factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the function with a sample number
num = int(input("Enter a number: "))
result = factorial(num)

# Displaying the factorial result
print(f"The factorial of {num} is {result}")