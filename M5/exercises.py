

def is_even(n):
    return n % 2 == 0


def integer_division(a, b):
    return a // b


def max(a, b):
    if a > b:
        return a
    return b


def sub_5_from_elements(lst):
    for i in range(len(lst)):  #  cant do for i in lst as the element wont change
        lst[i] -= 5


def sum_list(lst):
    #return sum(lst)
    total = 0
    for i in lst:
        total += i
    return total


def product_list(lst):
    product = 1
    for i in lst:
        product *= i
    return product


def mean_list(lst):
    return sum_list(lst) / len(lst)


def maximum_element(lst):
    biggest = lst[0]
    for i in lst[1:]:
        if i > biggest:
            biggest = max(biggest, i)

    return biggest


lst = [1, 2, 3, 4, 5]
print(mean_list(lst))
print(maximum_element(lst))
