s = 'sadman'
#indexing from front and from end
print(s[0]) # s
print(s[-1]) #n
print(s[-4]) #d
#slicing: extract a particular section
print(s[1:3]) # ad
print(s[3:]) #man
print(s[-1:]) #n
print(s[:-1]) #sadma
print(s[1:4:2])
print(s[::-1]) #namdas  makes reverse
print(s[::2])  #sda
print(s[0:4:2]) #That can be interpreted as: get every second element between indexes 0 and 4.
x     = [0,1,2,3]
x[:2] = ['AB','CD'] #put 'AB' and 'CD' in the previous indexes of 2
print(x)
y     = [0,1,2,3]
y[2:] =['AB','CD']
print(y)
a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
del a[::2]
print(a)
