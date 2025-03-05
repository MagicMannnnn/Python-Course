
for i in range(1, 101):
    modThree = i % 3
    modFive = i % 5
    if modThree == 0 and modFive == 0:
        print("fizzbuzz")
    elif modThree == 0:
        print("fizz")
    elif modFive == 0:
        print("buzz")
    else:
        print(i)
