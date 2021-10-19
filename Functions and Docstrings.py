# Buil-in Fuction
a = 9
b = 8
c = sum((a, b))
print(c)

# User-defined Function
def func1(c, d):
    print("Hello you are in func1", c + d)
func1(50, 60)

def func2(e, f):
    """This is a function which will calculate average of two numbers"""
    average = (e + f)/2
    return average
h = func2(60, 70)
print(h)
print(func2.__doc__)