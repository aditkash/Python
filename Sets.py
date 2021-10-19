# A set is a data structure, having unordered, unique, and unindexed elements.
# Sets are iterable (iterations can be performed using loops).
# They are mutable (can be updated by adding or removing entries).
# There is no duplication (two same entries do not occur).

s = set()
# print(type(s))
# l = [1, 2, 3, 4, 5]
# s_from_list = set(l)
# print(s_from_list)
# print(type(s_from_list))
s.add(1)
s.add(2)
s.remove(2)
# print(s)
s1 = {4,5}
print(s.isdisjoint(s1))