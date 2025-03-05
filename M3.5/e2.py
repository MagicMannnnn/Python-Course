
userInput = ""
while userInput != "y":
    n1 = int(input("n1: "))
    sign = input("sign: ")
    n2 = int(input("n2: "))
    if sign == "+":
        print(n1 + n2)
    elif sign == "-":
        print(n1 - n2)
    elif sign == "*":
        print(n1 * n2)
    elif sign == "/":
        print(n1 / n2)
    else:
        print("sign not in this calculator!")
    userInput = input("would you like to exit? (y/n) ")
    