
shoppingList = {}

userInput = ""

while userInput != "exit":
    print("\n\nShopping List: ")
    for key, value in zip(shoppingList.keys(), shoppingList.values()):
        print(f"{key}: {value}")
    print("\n")

    userInput = input("What would you like to do? \n1. add an item to the list\n\
2.remove items from the list\n3.edit an item\n")

    if userInput == "exit":
        break
    userInput = int(userInput)

    if userInput == 1:
        item = input("item to add: ")
        amount = int(input("how many: "))
        shoppingList[item] = amount + shoppingList.get(item, 0)  # will increase if key already in dict, or if key not in dict will be 0 plus the amount
    elif userInput == 2:
        item = input("item to remove: ")
        amount = int(input("how many: "))
        shoppingList[item] -= amount
        if shoppingList[item] <= 0:
            shoppingList.pop(item)
    elif userInput == 3:
        item = input("item to edit: ")
        editedItem = input("edited item: ")
        shoppingList[editedItem] = shoppingList[item]
        shoppingList.pop(item)
    else:
        print("not an option")
