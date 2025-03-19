
nWords = 0
with open("file.txt", "r") as f:
    for line in f.readlines():
        line = line.rstrip()  # removes whitespace at end of line
        nWords += len(line.split(" "))

with open("nWords.txt", "w") as f:
    f.write(f"number of words: {nWords}")
