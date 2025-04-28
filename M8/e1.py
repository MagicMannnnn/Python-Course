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


if __name__ == "__main__":
    print(getData())