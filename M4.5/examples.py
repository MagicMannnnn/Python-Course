
myDict = {"CustomerID": 1, "firstName": "George", "Age": 19}
print(myDict["CustomerID"])
print(myDict.get("CustomerID"))
print(myDict.get("CustomerID", 0))  # 0 is the default value - if key doesnt exist will return 0

for key in myDict.keys():
    print(myDict[key])

for value in myDict.values():
    print(value)

for key, value in zip(myDict.keys(), myDict.values()):
    print(f"{key}, {value}")




