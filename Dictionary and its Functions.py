# Dictionary is nothing but key value pairs.
# Python dictionary is an unordered collection of items.
# Each item of the dictionary has a key and value pair.
# Dictionaries are mutable.

d1 = {"Spiderman":"Peter", "Superman":"Clark", "Batman":"Bruce", "Shaktiman":"Gangadhar",
      "X-men":{"Professor X":"Patrick", "Cyclops":"Scott", "Wolverine":"Hugh", "Rough":"Anna"}}
d1["Deadpool"] = "Wade"
del d1["X-men"]
print(d1)
# print(d1["Batman"])
d2 = d1.copy()
d2.update({"Hulk":"Eric"})
print(d2)
print(d2.keys())
print(d2.items())