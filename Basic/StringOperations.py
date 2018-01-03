a = 3 * 'x'+ 'movie'
print(a)
print(a+' suck')
#slicing
b = 'soumik'
print(b[:2]+b[2:])
print('R'+b[1:])  # [1:] means from 1 (inclusive) but [:2] means the indexes before 2 and 2 is exclusive index:0 1

square = [1,4,9,16,25]
print(square[:]) #prints all
print(square) #prints all
print(square+[36,49])
square[2] =10  #List are mutable
print(square)
square.append(100)
print(square)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[1:4] =['B','C','D']
print(letters) #['a', 'B', 'C', 'D', 'e', 'f', 'g']
m = ['a','b','c']
n = [1,2,3]
z = [m,n]
print(z) #[['a', 'b', 'c'], [1, 2, 3]]
print(z[0]) #['a', 'b', 'c']
print(z[1]) #[1, 2, 3]                         0  1  2
                               #               -  -  -
print(z[0][1]) #b raw->0 and column->1    0|   a  b  c
                               #          1|   1  2  3
print(z[1][2]) #3





