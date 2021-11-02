# String formatting is used to design the string using formatting techniques provided by 
# the particular programming language.

# 1. String Formatting (% Operator):
# Python has a built-in operation that we can access with the % operator. 
# This will help us to do simple positional formatting.
name = "Jack"
n = "%s My name is %s" %name
print(n)

# 2. Using Tuple ():
# The string formatting syntax, 
# which uses % operator changes slightly if we want to make multiple substitutions in a single string. 
# The % operator takes only one argument, to mention more than one argument, use tuples.
name = "Jack"
Class = 5
s = "%s is in class %d" %(name, Class)
print(s)

# 3. String Formatting (str.format):
# format() string formatting method eliminates the %-operator special syntax and 
# makes the syntax for string formatting more regular. 
# str.format() allows multiple substitutions and value formatting. We can use format() to do simple positional formatting.
# Syntax: {}.format(values)
str = "This article is written in {}"
print (str.format("Python"))

# 4. Using f-Strings (f):
# Python added a new string formatting approach called formatted string literals or "f-strings."
# This is a new way of formatting strings.
# A much more simple and intuitive solution is the use of Formatted string literals.
str1 = "Python"
str2 = "Programming"
print(f"Welcome to our {str1}{str2} tutorial")

# Time Module:
# The time module provides time-related functions. It handles the time-related tasks.
# To use functions that are defined in this module, we need to import the module first.
import time
# It is mostly used in measuring the time elapsed during program execution.

# f-strings
import math

me = "Harry"
a1 =3
# a = "this is %s %s"%(me, a1)
# a = "This is {1} {0}"
# b = a.format(me, a1)
# print(b)
a = f"this is {me} {a1} {math.cos(65)}"
# time
print(a)