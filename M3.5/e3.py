
answer = "password1"
userInput = input("password: ")
while userInput != answer:
    print("wrong password!")
    userInput = input("password: ")
print("correct password!")
