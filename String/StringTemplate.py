from string import Template
students = [('Kabir',36,'Math'),('Kuddus',96,'English'),('Abul',69,'History')]
t=Template('Hi $name, your marks is $mark in $sub')
for i in students:
    print(t.substitute(name=i[0], mark=i[1], sub=i[2]))
