lst = [1, 2, 3, 4, 5]

for i in lst[::-1]:
    print(i)

for i in reversed(lst):
    print(i)

newlist = []
for i in lst:
    newlist.insert(0, i)

print(newlist)
