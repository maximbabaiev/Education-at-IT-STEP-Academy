user = {
    "1111": 'Tom',
    "2222": 'Dima',
    "3333": "sasha",
}
user1 = user.get("5555", 'Oleg')
user2 = user.get("2222")
user3 = user.get("3333")
print(user1, user2, user3)
del user["3333"]

print(user1, user2, user3)

print(user)