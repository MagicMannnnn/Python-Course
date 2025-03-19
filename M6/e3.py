
word = "new"
nWords = 0
with open("file.txt", "a+") as f:  # we need to use a+ so we can read and write from the file without deleting the data,
    f.seek(0)  # however the pointer will start at the bottom of the file, so to read the file we need to set the pointer to 0
    for line in f.readlines():
        line = line.rstrip()  # removes whitespace at end of line
        words = line.split(" ")
        nWords += words.count(word)

    f.write(f"amount of times the word {word} is in this file is: {nWords}\n")


