def is_armstrong(number):

    a = str(number)
    sum = 0
    for i in a:
        sum += int(i) ** len(a)

    if sum == number:
        return True
    else:
        return False
