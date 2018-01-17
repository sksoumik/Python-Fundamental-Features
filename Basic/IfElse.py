score = int(input('Enter your score'))
if score >= 90:
    print('A')
else:
    if score >= 80:
        print('B')
    else:
        if score >= 70:
            print('C')
        else:
            if score >= 60:
                print('D')
            else:
                print('F')


square_list = []
for s in range(1, 11):
    square_list.append(s*s)
print(square_list)

sq_list = [x * x for x in range(1, 11)]
print(sq_list)

sq_list = [x * x for x in range(1, 11) if x % 2 != 0]  # only for odd numbers
print(sq_list)

text = [ch.upper() for ch in 'comprehension' if ch not in 'aeiou']
print(text)  # ['C', 'M', 'P', 'R', 'H', 'N', 'S', 'N']
