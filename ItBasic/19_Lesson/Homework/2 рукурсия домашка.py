def printUserStar(n=int(input())):
    star = "*"
    if n == 1:
        return star
    else:
        return star + printUserStar(n - 1)


print(printUserStar())
