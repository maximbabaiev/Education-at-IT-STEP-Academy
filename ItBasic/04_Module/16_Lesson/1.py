# def replace(string, old_letters, new_letters):
#     new_string = ''
#     for element in string:
#         if element == old_letters:
#             new_string += new_letters
#         else:
#             new_string += element
#     return new_string
#
#
# new2 = replace("hello", "h", "g") + "!"
#
# print(new2)


# def counts_word(full_string):
#     count = 0
#     for e in full_string.split():
#         if e.istitle():
#             count += 1
#     return count
#
#
# print(counts_word(input("input str")))

# def counts_word(full_string):
#     count = 0
#     for e in full_string.split():
#         if not islower():
#             count += 1
#     return count
#
#
# print(counts_word(input("input str")))


# list_var = []
# for i in range(0, 101):
#     list_var.append(i)
# print(list_var)

# list_var = [i for i in range(0, 101) if i % 5 == 0 and i > 40]
#
# print(list_var)


# dict_var = {
#
# }
# string_var = input("enter your word: ")
# for e in string_var:
#     dict_var[e] = string_var.count(e)
# print(dict_var)

# string_var = input("enter your word: ")
# print({e: string_var.count(e) for e in string_var})

from random import randint

# list_var1 = [randint(1, 10) for i in range(10)]
# list_var2 = [randint(1, 10) for a in range(10)]

# print(list_var1)
# print(list_var2)


def middle_list(first_list, second_list):
    return tuple(e for e in first_list if e in second_list)


list_var1 = [randint(1, 10) for i in range(10)]
list_var2 = [randint(1, 10) for a in range(10)]

print(middle_list(first_list=list_var1, second_list=list_var2))





