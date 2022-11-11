def main():
    list_of_strings = ["Список - изменяемый тип данных", "Строка - неизменяемый тип данных",
                       "Строковый метод работает быстрее, чем срез",
                       "Для обхода последовательности используйте совместный цикл"]
    # return [element for element in list_of_strings if element.lower().startswith("с")]
    # return [element for element in list_of_strings if "тип данных" in element]
    # return {elem: len(elem) for elem in list_of_strings}
    return {elem: {symbol: elem.count(symbol) for symbol in elem} for elem in list_of_strings}

print(main())

