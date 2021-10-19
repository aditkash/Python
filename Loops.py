# 'For Loops'
# Applicable for List - [], Tupple - () and Dictionary - {}.
print("*** For Loops ***")
list  = ["Alex", "Scott", "Max", "Jeff", "Corey"]
for item in list:
    print(item)

list1 = [["Alex", 1], ["Scott", 2], ["Max", 3]]
for item, lollypop in list1:
    print("For", item, "lollypop is", lollypop)

dict1 = dict(list1)
print(dict1)
for item, lollypop in dict1.items():
    print("For", item, "lollypop is", lollypop)
for item in dict1:
    print(item)

# Quizz - Prepare a list with any item in it and print the item only if it is > 6.
print("*** Quizz ***")
list2 = ["Jeff", 3, 6, "New York", 10, "Apple", 34, 90]
for item in list2:
    if str(item).isnumeric() and item>6:
        print(item)

# 'While Loops'
# A while loop in python runs a bunch of code or statements again and again until
# the given condition is true when the condition becomes false, the loop terminates its repetition.
# The condition could be either true or false.
print("*** While Loops ***")
i = 0
while(i<40):
    print(i)
    i = i + 2

# Difference between 'For' and 'While' loops:
# 'for' loop runs until the iteration through, set, lists, tuple, etc, or a generator function is completed.
# In the case of a 'while' loop, the statement simply loops until the condition we have provided becomes false.