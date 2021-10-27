# Instructions:
# You have to take an integer type variable, and the input of the variable will define the length of the triangle.
# You have to declare another Boolean variable.
# When the value of Boolean is 1 i.e. True, the pattern will be printed in ascending order.
# But if the value of Boolean is 0 or false, then the triangle will be printed upside down.

a = int(input("Please add no. of lines you want to print:"))
b = bool(int(input("Please add 0 for false:")))

def star(a,b):
    if b == True:
        c = 1
        while c <= a:
            print(c * "*")
            c = c + 1
    else:
        while a > 0:
            print(a * "*")
            a = a - 1
star(a,b)