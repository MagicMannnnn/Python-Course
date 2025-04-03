
def getAmount(minimumAmount=1):
    correctAmount = False
    amount = 0
    while not correctAmount:
        try:
            amount = int(input("how many: "))
            correctAmount = amount >= minimumAmount
        except ValueError:
            print("Needs to be an integer amount, please try again.")
    return amount


def addItem(shoppingList):
    item = input("item to add: ")
    shoppingList[item] = getAmount() + shoppingList.get(item, 0)


def removeItem(shoppingList):
    if len(shoppingList.keys()) == 0:
        print("you have no items in the list")
        return
    item = input("item to remove: ")
    while item not in shoppingList.keys():
        print("item not in list, please try again.")
        item = input("item to remove: ")
    shoppingList[item] -= getAmount(minimumAmount=0)
    if shoppingList[item] <= 0:
        shoppingList.pop(item)


def editItem(shoppingList):
    if len(shoppingList.keys()) == 0:
        print("you have no items in the list")
        return
    item = input("item to edit: ")
    while item not in shoppingList.keys():
        print("item not in list, please try again.")
        item = input("item to edit: ")
    editedItem = input("new item: ")
    shoppingList[editedItem] = shoppingList[item]
    shoppingList.pop(item)


def Main():
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
        try:
            userInput = int(userInput)
        except ValueError:
            print("not an option.")
            continue

        if userInput == 1:
            addItem(shoppingList)
        elif userInput == 2:
            removeItem(shoppingList)
        elif userInput == 3:
            editItem(shoppingList)
        else:
            print("not an option")


if __name__ == "__main__":
    Main()
