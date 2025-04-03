
integers = [1, 2, 3, 4, 5, 6, 7]

with open("../M7/integers.txt", "w") as f:
    integersAsStrings = [f"{i}\n" for i in integers]
    f.writelines(integersAsStrings)
