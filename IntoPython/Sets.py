my_set={3,4,5,6,1,2,7}
your_set={'3 Idiots', 'Rang de Basanti','PK',3}
print(my_set|your_set)
print(my_set.union(your_set))
print(my_set.intersection(your_set)) #return common element
print(my_set-your_set)
print({3,4}.issubset(my_set))
print({10,11}.issubset(my_set))
your_set.clear()
print("your_set value now:",your_set)