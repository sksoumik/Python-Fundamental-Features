i = 5


def f(arg=i):
    print(arg)


i = 6

f()


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(10))


# --------------
def fx(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(fx(1))
print(fx(2))
print(fx(3))

