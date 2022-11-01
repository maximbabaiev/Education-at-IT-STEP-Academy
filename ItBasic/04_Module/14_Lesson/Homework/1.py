


def Check_Vow(string, vowels): # создаем функцию
    string = string.casefold() # переводим строку в нижний регистр
    count = {}.fromkeys(vowels, 0) # создаем словарь где кулюч гласная а значение это ее количество
    for i in string: # пошли циклом по строке

        if i in count:
            count[i] += 1 # находим и добавляем в count
    return count


vowels = 'aeiou'

string = "frjfvwjfHGJHVJHVHJBLUIOAKMLiduiudygdcafcd"

print(Check_Vow(string, vowels))
