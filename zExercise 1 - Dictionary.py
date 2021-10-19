dict = {"clear()"    : "Removes all the elements from the dictionary",
        "copy()"     : "Returns a copy of the dictionary",
        "fromkeys()" : "Returns a dictionary with the specified keys and value",
        "get()"      : "Returns the value of the specified key",
        "items()"    : "Returns a list containing a tuple for each key value pair"}

print("Please type your from the following functions:\n" "clear(), " "copy(), " "fromkeys(), " "get(), " "items()")
inpwrd = input()
print("The meaning of your word is:")
print(dict[inpwrd])