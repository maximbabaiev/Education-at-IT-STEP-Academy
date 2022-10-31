list1 = [12, 34, 56, 67, 45]

searchEl = 12


def search(my_list, platform):
    for i in range(len(my_list)):
        if my_list[i] == platform:
            return True
    return False


if search(list1, searchEl):
    print("Number is found")
else:
    print("Number does not found")