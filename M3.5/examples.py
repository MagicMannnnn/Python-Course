
x = True
while x:
    if input("quit? (y/n): ").lower() == "y":
        x = False


answer = "password1"
userInput = input("password: ")
while userInput != answer:
    print("wrong password!")
    userInput = input("password: ")
print("correct password!")

for i in range(5):
    print(i)
    if i == 3:
        break

print("")

for i in range(5):
    if i == 3:
        continue
    print(i)

while True:
    #  code here
    exitLoop = input("continue? (y/n): ")
    if exitLoop.lower() == "n":
        break


for index, item in enumerate("hello"):
    print(f"{index} : {item}")
