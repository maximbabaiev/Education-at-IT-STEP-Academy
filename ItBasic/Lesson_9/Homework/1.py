import random

print("Welcome to game: \'Rock, paper, scissors\'")
print("The game will go against the computer")
print("[R] - rock")
print("[S] - scissors")
print("[P] - paper")

user_score = 0
user_choice = 0
bot_score = 0
bot_choice = 0
user_win = 0
bot_win = 0

print("---GAME START---")
while True:
    for i in range(3):
        print("---ROUND №", str(i + 1), "---")
        bot_choice = random.choice(["R", "S", "P"])
        user_choice = input("Your choice\n")
        print("You: ", user_choice, "& Bot choice: ", bot_choice)
    if user_choice == bot_choice:
        print("Draw")
    elif user_choice == "R":
        if bot_choice == "S":
            user_score += 1
            print("Player won round")
        else:
            bot_score += 1
            print("Bot won")
    elif user_choice == "S":
        if bot_choice == "P":
            user_score += 1
            print("Player won round")
        else:
            bot_score += 1
            print("Bot won")
    elif user_choice == "P":
        if bot_choice == "R":
            user_score += 1
            print("Player won round")
        else:
            bot_score += 1
            print("Bot won")
    else:
        print("Error")

    print("Player score: ", user_score, "Bot score: ", bot_score)
    if user_score > bot_score:
        user_win += 1
        print("Player win")
    elif bot_score > user_score:
        bot_win += 1
        print("Bot win")
    else:
        print("Draw")
    x = input("Try again? [Yes] or [No]\n")
    if x == "No":
        print("Player win: ", user_win, "\nBot win: ", bot_win)
        print("Goodbye!")
        break
    elif x == "Yes":
        print("Let's play!")
        continue
