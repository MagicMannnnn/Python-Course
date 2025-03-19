
lst = ["h", "e", "l", "l", "o"]
print(lst[0])
print(lst[-1])

lst[0] = "q"

lst.append("z")
print(lst)

lst.pop()
print(lst)
lst.pop(1)
print(lst)

lst.remove("l")

lst.insert(3, "!")

print(lst.index("!"))

print(len(lst))


lst = [3, 7, 13, 2, 5, 9, 6]
print(max(lst))
print(min(lst))

#  format = lst[first:last:step] -> first inclusive, last not inclusive

firstThree = lst[:3]
thirdOnwards = lst[3:]
lastThree = lst[-3:]
everyOther = lst[::2]
backwards = lst[::-1]

print(firstThree)
print(thirdOnwards)
print(lastThree)
print(everyOther)


for i in lst: # iterates over every item
    print(i)

s = "hello"
print(list(s))

s = "hello everyone"
lst = s.split(" ")
print(lst)

lst = ["h", "e", "l", "l", "o"]
s = "".join(lst)
print(s)



