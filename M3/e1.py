
x = int(input("number: "))
if x % 2 == 0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")
# OR
s = "odd"
if x % 2 == 0:
    s = "even"
print(f"{x} is {s}")  # less code, however less readable
