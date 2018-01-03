import math
try:
    x= int(input('Enter a value for sqrt: '))
    print(math.sqrt(x))
except:
    print('You can\'t enter a negative value')