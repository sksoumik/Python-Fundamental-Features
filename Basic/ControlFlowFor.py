course = ['ENG', 'CSE327', 'CSE323', 'MAT361']
for c in course:
    print(c, len(c))

for c in course[:]:
    if len(c) > 5:
        course.insert(0, c)
print(course)
