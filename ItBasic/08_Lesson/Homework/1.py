mytext = "The user enters some text from the keyboard, and then — list of reserved words."
mytext1 = mytext.lower()
list1 = list(mytext.split())
listnew = list(mytext1.split())
text = ["user", "from", "and"]
for i in range(len(listnew)):
    for p in text:
        if p in listnew[i]:
            list1[i] = listnew[i].upper()

print(' '.join(list1))



