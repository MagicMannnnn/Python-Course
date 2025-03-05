
s = "hello"
print(len(s))

x = int(input("number: "))
if x > 3:
    print("Bigger than 3")
elif x < 3:
    print("Less than 3")
else:
    print("Three!")

a = True
if a and x == 3:
    print("crazy")

for i in range(5):
    print(i)

print("")

for i in range(1, 6):
    print(i)

print("")

s = "hello"
for i in range(len(s)):
    print(s[i])

print(s)

for i in range(3):
    x = int(input(f"number {i+1}: "))
    remainder = x % 3
    if remainder == 0:
        print("Factor of 3!")
    else:
        integerDivision = x // 3
        print(f"{x} / 3 = {integerDivision} remainder {remainder}")


