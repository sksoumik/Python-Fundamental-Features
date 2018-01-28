# Birthday DB. If name exists, shows the birth date or else it asks for the birth date of that person
# blank space to exit from app

birthday = {'Dourjoy': '30 April', 'Nahid': '20 November', 'Irtiza': '15 March'}

while True:
    print("Enter a name: (blank to quit)")
    name = input()

    if name == '':
        break
    if name in birthday:
        print(birthday[name] + ' is the birthday of ' + name)
    else:
        print("I do not have any information for " + name)
        print("What is his/her birthday? ")
        bday = input()
        birthday[name] = bday
        print("Birthday Database Updated")
