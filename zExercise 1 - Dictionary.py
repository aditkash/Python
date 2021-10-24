dict = {"clear()"    : "removes all the elements from the dictionary",
        "copy()"     : "returns a copy of the dictionary",
        "fromkeys()" : "returns a dictionary with the specified keys and value",
        "get()"      : "returns the value of the specified key",
        "items()"    : "returns a list containing a tuple for each key value pair"}

print("Please type your from the following functions:\n" "clear(), " "copy(), " "fromkeys(), " "get(), " "items()")
inpwrd = input()
print("The " + inpwrd + " function " + dict[inpwrd])