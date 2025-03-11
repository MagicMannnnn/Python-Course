
shoppingList = []

userInput = ""

while userInput != "exit":
    print("\n\nShopping List: ")
    for i in shoppingList:
        print(i)
    print("\n")

    userInput = input("What would you like to do? \n1. add an item to the list\n\
2.remove an item from the list\n3.remove the last item added\n4.edit an item\n")

    if userInput == "exit":
        break
    userInput = int(userInput)

    if userInput == 1:
        item = input("item to add: ")
        shoppingList.append(item)
    elif userInput == 2:
        item = input("item to remove: ")
        shoppingList.remove(item)
    elif userInput == 3:
        shoppingList.pop()
    elif userInput == 4:
        item = input("item to edit: ")
        index = shoppingList.index(item)
        editedItem = input("edited item: ")
        shoppingList[index] = editedItem
    else:
        print("not an option")
