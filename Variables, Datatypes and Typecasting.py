# Variables
var1 = "Hello world"
var2 = 4
var3 = 36.7

'''
type() function is a function that allows a user to find data type of any variable. 
It returns the data type of any data contained in the variable passed to it.
'''
print(type(var3))

# Datatypes
# str() int() float()
print(int(var2+var3))

'''
Typecasting: Typecasting is the way to change one data type of any data or variable to another datatype,
i.e. it changes the data type of any variable to some other data type.
'''
print(10 * "Hello world\n")
print(5 * str(int(var2) + int(var3)))

print("Enter your number")
inpnum = input()
print("You entered", int(inpnum) + 10)

# Quizz - Preparing a calculator that adds up two numbers
print("Enter your first number")
inpnum1 = input()
print("Enter your second number")
inpnum2 = input()
print("The sum of your numbers is", int(inpnum1) + int(inpnum2))