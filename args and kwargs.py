# Asterisk is used in python as a mathematical symbol for multiplication,
# but in case of arguments, it refers to unpacking.
# The unpacking could be for a list, tuple, or a dictionary.
# In Python programming, there are two types of arguments that can be passed in a function:

# 1. Positional arguments:
# Positional arguments are the one in which an order has to be followed while passing arguments.
# *args:
# args is a short form used for arguments.
# It is used to unpack an argument. In the case of *args, the argument could be a list or tuple.
# Eg. Suppose that we have to enter the name of students who attended a particular lecture. 
#     Each day the number of students is different, so positional arguments would not be helpful because
#     we can not leave an argument empty in that case.
#     So the best way to deal with such programs is to
#     define the function using the class name as formal positional argument and student names with parameter *args.
#     In this way, we can pass student's names using a tuple.
# The name 'args' does not make any difference, we can use any other name, such as *myargs.
# The only thing that makes a difference is the Asterisk(*).

# 2. Keyword arguments:
# **kwargs:
# The full form of **kwargs is keyword arguments.
# It passes the data to the argument in the form of a dictionary,
# that is in the form of key and value pair.

def func(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

har = ["Harry", "Rohan", "Skillf", "Hammad", "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor", "The Programmer": "Coordinator", "Shivam":"Cook"}
func(normal, har, kw)