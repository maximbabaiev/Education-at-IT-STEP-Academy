import random

# products = ["tomatoes", "patatoes", "cucumbers", "bread", "burito"]
# print("Randomm product", random.choice(products))
# products = [2, 3, 56, 67, 68]
# random.shuffle(products)
# print("Random shuffle", products)
cards = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
random.shuffle(cards)

print("Lets play BlackJack?")
count_player = 0
count_bot = 0

while True:
    choice = input("Take card? y/n\n")
    if choice == "y":
        current = cards.pop()
        current_bot = cards.pop()
        print("You take", current)
        count_player += current
        count_bot += current
        if count_player > 21:
            print("You loose. You have", count_player, "Bot win", count_bot)
            break
        elif count_player == 21:
            print("You win. You have", count_player, "Bot loose", count_bot)
            break
        else:
            print("You score: ", count_player)
    elif choice == "n":
        print("Count: ", count_player)
        break
print("See U again")