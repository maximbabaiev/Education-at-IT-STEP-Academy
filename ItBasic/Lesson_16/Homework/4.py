
def square(long, symbol, choice):
    square_var = ""
    if choice:
        for i in range(long):
            square_var += f"{(symbol + ' ' )* long}\n"
    else:
        square_var = f'{(symbol + " ") * long}\n'
        for i in range(long - 2):
            square_var += f'{symbol + " "}{"  " * (long - 2)}{symbol + " "}\n'
        square_var += f'{(symbol + " ") * long}\n'
    return square_var


print(square(long=10, symbol="*", choice=False))