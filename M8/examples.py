import csv

def getData(filename="data.csv"):
    data = []
    with open("data.csv", "r") as f:
        reader = csv.reader(f)

        reader.__next__() #skips the top row, only neccessary if top row isnt data
        for row in reader:
            try: # convert to correct data formatting
                row[0] = int(row[0]) # duration
                row[1] = int(row[1]) # pulse
                row[2] = int(row[2]) # max pulse
                row[3] = float(row[3]) # calories
                data.append(row)
            except ValueError: #maybe missing data, or empty line
                pass

    return data

def writeData(data, filename="example.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)


def Main():
    arr = [["0 0", "0, 1"], ["1, 0", "1, 1"]] #indexes
    print(arr[1])
    print(arr[0][1])

    print("\n")

    for row in arr:
        for item in row:
            print(item)




if __name__ == "__main__":
    Main()
    data = getData()
    print(data)
    writeData(data)

