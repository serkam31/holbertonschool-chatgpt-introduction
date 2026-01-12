#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Calculate the factorial of a given number using recursion.
    
    Parameters:
        n (int): A non-negative integer for which to calculate the factorial.
    
    Returns:
        int: The factorial of the input number n.
    """
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Get the number from command-line arguments
number = int(sys.argv[1])

# Calculate factorial
f = factorial(number)

# Print the result
print(f)
