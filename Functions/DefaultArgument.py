def student(name, score):
    print(name, 'Scored', score, 'marks')


student('Soumik', 70)


def student(name='Kabir', cgpa=3.11):
    print(name, '\'s cgpa is', cgpa)


student()


# Correct way of writing empty function
def fun():
    pass  # pass does nothing. It only works as a dummy statement.


mutex = True
if mutex:
    print('True')
else:
    pass  # do nothing


