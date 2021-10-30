# It is also known as anonymus fuction
# Lambda expression is a function definition that is not bound to an identifier (def).
# The anonymous function is an inline function. 
# The anonymous functions are created using a lambda operator and cannot contain multiple expressions.

# Significant Differences Between Lambda Expressions And Simple Functions:
# 1. Can be passed immediately with or without variables.
# 2. They are inline functions.
# 3. Automatic return of results.
# 4. There is neither a document string nor a name.

# Python List sort():
# Sorting means arranging data systematically. 
# If the data we want to work with is not sorted, we will face problems finding the desired element.
# The Python language, like other programming languages, can sort data.
# Python has an in-built method i.e. sort(), which is used to sort the elements of the given list in a specified ascending or descending order. 
# There is also a built-in function # i.e. sorted(), that builds a new sorted list from an iterable like list, dictionary, etc.
# The syntax of the sort() method is:
# list.sort(key=myFunc ,reverse=True|False)
# Parameter Values:
# key:
# In the key parameter, we specify a function that is called on each list element before making comparisons.
# reverse
# This is optional. False will sort the list in ascending order, and true will sort the list in descending order.
# Default is reverse=False.

# Simple function:
def add(a,b):
    return a + b
print(add(4,6))

# Lambda function:
plus = lambda x, y: x + y
print(plus(4,6))

# sort:
a = [[1,14], [5,6], [8,23]]
a.sort(key=lambda x: x[1])
print(a)