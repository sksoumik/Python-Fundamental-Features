# There are three dictionary methods
# keys()  ||  values()  ||  items()

spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)     # prints red & 42

for v in spam.keys():
    print(v)     # prints color & age

for v in spam.items():
    print(v)      # ('color', 'red')   # ('age', 42)

# we can also do these things like below
print(spam.keys())
print(spam.values())
print(spam.items())

# we can also display the items like a list
print(list(spam.values()))
print(list(spam.keys()))
print(list(spam.items()))



