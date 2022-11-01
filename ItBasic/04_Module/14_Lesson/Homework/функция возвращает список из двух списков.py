list1 = ["marina", "petia"]
list2 = ["13", "14"]


def cont(a, b):
    firstList = []
    for i in range(len(a)):
        firstList.append(a[i])
        firstList.append(b[i])
    return firstList


print(cont(list1, list2))
