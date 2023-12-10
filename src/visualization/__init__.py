import pandas as pf

# BEGIN: FILEPATH
def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

# Example usage
number = 8
if is_fibonacci(number):
    print(f"{number} is a Fibonacci number")
else:
    print(f"{number} is not a Fibonacci number")
# END: FILEPATH





print('Hello world')
