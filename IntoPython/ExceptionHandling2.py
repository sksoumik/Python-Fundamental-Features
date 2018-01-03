import math
x=int(input('Enter a value:'))
if x<0:
    raise RuntimeError('You can\'t enter negative number for square root')
else:
    print(math.sqrt(x))