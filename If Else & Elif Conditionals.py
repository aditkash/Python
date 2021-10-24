# Quizz - Whether a person can drive or can't drive based on his age.
print("What's your age?")
age = int(input())
if age>18:
    print("You can drive!")
elif age==18:
    print("Physical driving test required.")
elif age<18:
    print("Sorry, you can't drive!")

# Short Hand If Else Notation
print("*** Short Hand If Else Notation ***")
a = int(input("enter a\n"))
b = int(input("enter b\n"))
# if a > b: print("A is greater than B")
# print("B is greater than A") if a < b else print("A is greater than B")