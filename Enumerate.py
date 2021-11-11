# An enumerate is a built-in function that provides an index to data structure elements, 
# making iterations through them easier and simpler.
# What enumerate function does is, 
# it assigns an index to every element or value in the object that we want to iterate, 
# so we do not have to assign a specific variable for incremental function, instead we have to apply a for loop, and
#  our function will start working.
# Syntax: enumerate(iterable, start=0)
# When calling a simple enumeration function, we have to provide two parameters:
# 1. The data structure that we want to iterate
# 2. The index from where we want to start our iteration
# Note: The iterable must be an object that supports iteration

l = ["Paste", "Soap", "Comb", "Ditergent", "Maggie"]

for index, item in enumerate(l):
    if index%2==0:
        print(f"Javis, please buy {item}")