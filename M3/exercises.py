
x = int(input("number: "))
if x % 2 == 0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")
# OR
s = "odd"
if x % 2 == 0:
    s = "even"
print(f"{x} is {s}")  # This is shorter code, however less readable

for i in range(1, 13):
    print(f"{x} x {i} = {x*i}")

for i in range(1, 101):
    three = i % 3
    five = i % 5
    if three == 0 and five == 0:
        print("fizzbuzz")
    elif three == 0:
        print("fizz")
    elif five == 0:
        print("buzz")
    else:
        print(i)
