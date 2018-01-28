# Dictionaries vs. Lists
# Items in dictionaries are unordered. The first item in a list
# named spam would be spam[0]. But there is no “first” item in a dictionary.
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon)  # False   -- Order matters


eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)  # True   -- Order doesn't matter



