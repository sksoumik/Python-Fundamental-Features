user_name = input('Please enter your name: ')
print('your name in all capitals is ', user_name.upper(), ' and has length ', len(user_name))
print('your name in all capitals is ', user_name.capitalize(), ' and has length ', len(user_name))
user_radius = input('Enter the radius')
radius = float(user_radius)
diameter = radius * 2
print(diameter)
print('Sadman', 'Soumik', sep='***')  # Sadman***Soumik
print('Sadman', 'Soumik', end='***')  # Sadman Soumik***
name = 'Soumik'
age = 22
print('\n %s is your name and %d is your age' % (name, age))
price = 200
item = "Banana"
print('The %10s costs %5.2f cents' % (item, price))

