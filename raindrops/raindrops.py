def convert(number: int) -> str:
    x = ""

    if number % 3 == 0:
        x = x + "Pling"
    if number % 5 == 0:
        x = x + "Plang"
    if number % 7 == 0:
        x = x + "Plong"
    if not x:
        x = str(number)
    return x
