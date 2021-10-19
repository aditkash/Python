# List (is mutable)
numbers = [2, 7, 9, 11, 3]
numbers.remove(7)
numbers.pop()
numbers.sort()
numbers.append(90)
numbers[1] = 77

# Tuple (is immutable)
tp = (4, 2, 67, 0, 56)
tp1 = (5,) # Tuple with single value i.e. 5 (When a comma is added it becomes tuple)

# Swapping of two numbers
a = 10 
b = 15
print(a,b) #It will give output as: 10 15
a,b = b,a 
print(a,b) #It will give output as: 15 10