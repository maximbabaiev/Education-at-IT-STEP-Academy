list1 = [12, 34, 56, 67, 45]


def maxSum(list_max):
    maxint = list_max[0]
    for i in list_max:
        if i > maxint:
            maxint = i
    return maxint


print(maxSum(list1))
