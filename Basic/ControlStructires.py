counter = 1
while counter <= 5:
    print('Control Structures')
    counter = counter+1

for item in [1, 2, 3, 4, 5]:
    print(item, end=' ')


print()
for item in range(5):
    print(item*2, end=' ')


print()
for item in range(5):
    print(item ** 2, end=' ')


print()
animal_list = ['dog', 'cat', 'tiger']   # int object is not iterable
creature = []
for animal in animal_list:
    for cr in animal:
        creature.append(cr)
print(creature)

