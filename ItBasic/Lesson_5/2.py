health_pers = 10
attack_pers = 5
health_spider = 5
put = input("Куда мдем?Можем пойти [vlivo][vpravo] ")
if (put == "vlivo"):
    attack_pers += 5
    print("Вы получли меч, поздравляем!")
    if (put == "vpravo"):
        print("Позравлем вы победили!")
        print("Вы получили 1000000 XP")
        print("Теперь ваш уровень 99")

    else:
