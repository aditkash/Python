# Recursion occurs when a function calls itself.
# Mostly both recursion and iteration are used in association with loops.
# In both recursion and iteration, 
# The goal is to execute a statement again and again until a specific condition is fulfilled.
# An "iterative" loop ends when it has reached the end of its sequence; 
# Eg. if we are moving through a list, then the loop will stop executing when it reached the end of the list.
# In the case of "recursion", the function stops terminating when a base condition is satisfied.

# n! = n * n-1 * n-2 * n-3.....1 iterative method
# n! = n * (n-1)!
def factorial_iterative(n):
    """
    :param n: Integer
    :return: n * n-1 * n-2 * n-3.....1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

def factorial_recursive(n):
    """
    :param n: Integer
    :return: n * n-1 * n-2 * n-3.....1
    """
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
# 5 * factorial_recursive(4)
# 5 * 4 * factorial_recursive(3)
# 5 * 4 * 3 * factorial_recursive(2)
# 5 * 4 * 3 * 2 * factorial_recursive(1)
# 5 * 4 * 3 * 2 * 1 = 120

# ***Quiz***
# Fibonacci Sequence
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = int(input("Enter then number:"))
print("Factorial Using Iterative Method", factorial_iterative(number))
print("Factorial Using Recursive Method", factorial_recursive(number))
print(fibonacci(number))