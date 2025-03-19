

with open("file.txt", "r") as f:
    for line in f.readlines():
        line = line.rstrip()  # removes whitespace at end of line
        print(line)
