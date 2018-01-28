# Data types and declaration of Dictionary in Python
myCat = {'size': 'fat', 'color': 'grey', 'disposition': 'loud'}
print(myCat['size'])
print("My cat has " + myCat['color'] + ' fur')

# Dictionaries can still use integer values as keys,
# just like lists use integers for indexes, but they do not have to start at 0 and can be any number.
spam = {1511109042: 'My ID number', 1995:'Birth Year'}
print(spam[1511109042])

# For concatenating String we use + sign and for Integers we use , (comma)
spam = {'ID': 1511109042, 'year': 1995}
print('ID is :', spam['ID'], 'and Birth Year is :', spam['year'])



