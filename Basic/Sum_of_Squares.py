
N = input()
numArray = map(int, input().split())
sum_integer = 0
for i in numArray:
    sum_integer = sum_integer+(i*i)

print(sum_integer)