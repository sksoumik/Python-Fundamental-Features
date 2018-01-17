shopping_cart = {}
print("""
Select Shopping Cart options
-------------------------
option 1: add an item
option 2: remove an item
option 3: display items
option 0: exit shopping""")
option = int(input("Enter an option: "))
while option != 0:
    if option == 1:
        item = input("add an item")
        quantity = int(input("Enter quantity"))
        shopping_cart[item] = quantity
    elif option == 2:
        item = input('Enter the item to be removed')
        del(shopping_cart[item])
    elif option == 3:
        for item in shopping_cart:
            print(item, ":", shopping_cart[item])
    elif option != 0 :
        print("Invalid number choice")
    option = int(input("\nEnter an option"))
else:
    print("Shopping cart program closed")
