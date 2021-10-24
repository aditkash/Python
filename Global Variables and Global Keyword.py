# Local Varialble
def sum():
    a = 10 #Local Variable cannot be accessed outside the function.
    b = 20
    sum = a + b
    print(sum)
# print(a) #This gives an error.

# Global Variable
a = 1 #Global Variable
def print_Number():
    # a = a + 1
    print(a)
print_Number()

# Rules of 'global' keyword:
# 1. If we assigned a value to a variable within the function body,
#    it would be local unless explicitly declared as global.
# 2. Those variables that are referenced only inside a function are implicitly global.
# 3. There is no need to use the global keyword outside a function.

# l = 10 # Global
# def function1(n):
#     # l = 5 #Local
#     m = 8 #Local
#     global l
#     l = l + 45
#     print(l, m)
#     print(n, "I have printed")
# function1("This is me")
# # print(m)

x = 89
def harry():
    x = 20
    def rohan():
        global x
        x = 88
    # print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)
harry()
print(x)