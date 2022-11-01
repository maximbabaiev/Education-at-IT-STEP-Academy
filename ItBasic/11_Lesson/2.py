contactList = [
    ("Jon", 30),
    ("Davis", 31),
    ("Gonzales", 32),
    ("Harris", 35),
    ("Kelly", 37),
]

result = input()
first = dict(contactList)
if result in first:
    print(result + " - " + str(first[result]))
else:
    print("Not found")

