

with open("file.txt", "r") as f:
    for line in f.readlines():
        line = line.rstrip()  # removes whitespace at end of line
        print(line)

with open("file.txt", "a") as f:
    f.write("new line here\n")


with open("file2.txt", "a+") as f:
    f.write("hello\n")
    f.seek(0)
    lines = f.readlines()

    for line in lines:
        print(line)
    print(lines)

lines = ["line 1", "line 2", "line 3"]

with open("file3.txt", "w") as f:
    newLines = [line + "\n" for line in lines]  # use list comprehension to add a new line at the end of every line
    f.writelines(newLines)
