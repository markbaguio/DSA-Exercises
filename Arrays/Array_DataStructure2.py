"""You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)"""

heroes = ["Spider-Man", "Thor", "Hulk", "Iron Man", "Captain America"]

# 1
print("1.", len(heroes))

# 2
heroes.append("Black Panther")
print("2.", heroes)

# 3
heroes.pop()  # default is the last element in an array, in this case, "Black Panther."
heroes.insert(3, "Black Panther")
print("3.", heroes)

# 4
# print("4.", heroes.remove("Thor",), heroes.remove(
#     "Hulk"), heroes.insert(2, "Doctor Strange"))

heroes.remove("Thor"), heroes.remove("Hulk"), heroes.insert(
    1, "Doctor Strange"), print("4.", heroes)

# 5
heroes.sort()
print("5.", heroes)


# SOLUTION
# heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
# # 1. Length of the list
# print(len(heros))
# # 2. Add 'black panther' at the end of this list
# heros.append('black panther')
# print(heros)
# # 3. You realize that you need to add 'black panther' after 'hulk',
# # so remove it from the list first and then add it after 'hulk'
# heros.remove('black panther')
# heros.insert(3, 'black panther')
# print(heros)
# # 4. Now you don't like thor and hulk because they get angry easily :)
# #    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# #    Do that with one line of code.
# heros[1:3] = ['doctor strange']
# print(heros)
# # 5. Sort the list in alphabetical order
# heros.sort()
# print(heros)
