
def Main(output="hello"):
    print(output)

    x = "TypeError"
    #5 + x

    x = "ValueError"
    #int(x)

    lst = ["IndexError"]
    #lst[1]

    myDict = {"KeyError": 1}
    #myDict["key not here"]

    #x = 5
    try:
        print(5 + x)
    except:
        print("x is not a numerical value")
    finally:
        print("this will print whatever happens")

    x = 5
    if type(x) is not int:
        raise Exception("X is not an Integer")
    else:
        print(x**2)

    tup = (1, 2, 3, 4, 5) #immutable
    #tup[0] = 3 #value error
    tup = (5, 4, 3, 2, 1)
    print(tup)

    lst = [str(i) for i in tup]
    print(lst)


if __name__ == "__main__":
    Main()

