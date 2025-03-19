#
#
# def max_of_2_numbers(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
#
# def add_item_to_list(lst, x):
#     lst.append(x)
#
#
# x = max_of_2_numbers(3, 7)
#
# print(x)
#
# lst = [1, 2]
# print(lst)
#
# add_item_to_list(lst, 3)
#
# print(lst)
#
# add_item_to_list(lst.copy(), 4)
#
# print(lst)

def get_n_arrays(n):
    for i in range(n):
        lst = []
        for j in range(n):
            lst.append(i)
        yield lst


print(get_n_arrays(10))
print(type(get_n_arrays(10)))
for i in get_n_arrays(10):
    print(i)