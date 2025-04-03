
def Main(filename="integers.txt"):
    with open(filename, "r") as f:
        integers = []
        for line in f.readlines():
            line.rstrip()  # not actually needed when converting to integer, but could be useful for readability or if # strings being used
            try:
                integers.append(int(line))
            except TypeError:
                pass

    return integers


if __name__ == "__main__":
    print(Main())


