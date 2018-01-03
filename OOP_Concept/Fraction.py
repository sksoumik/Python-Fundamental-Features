def GCD(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n
class Fraction:
    def __init__(self,top,bottom):
        self.num=top
        self.den=bottom

    def show(self):
        print(self.num,"/",self.den)

    def __str__(self):
        return str(self.num) +"/"+str(self.den)



    def __add__(self, other_f):
        new_num = self.num*other_f.den + self.den*other_f.num
        new_den = self.den * other_f.den
        common = GCD(new_num,new_den)
        return Fraction(new_num//common,new_den//common)





#DRIVER program
my_f = Fraction(5,9)
my_f.show()

print('I ate ', my_f, ' of my pizza ')

f1 = Fraction(1,5)
f2 = Fraction(2,6)
f3 = f1+f2
print(f3)


