for x in range(5):
    print(x, end=' ')

print('\n')
for x in range(5, 10):
    print(x, end=' ')  # 5 6 7 8 9
print('\n')
for x in range(0, 10, 3):
    print(x, end=' ')  # 0 3 6 9

print('\n')
for x in range(-10, -100, -20):
    print(x, end=' ')  # -10 -30 -50 -70 -90
print('\n')
subject = ['English', 'Math', 'Computer Science', 'Software Engineering']
for i in range(len(subject)):
    print(i, subject[i])
