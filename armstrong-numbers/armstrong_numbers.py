def is_armstrong_number(self):

    order = len(str(self))
    sum = 0
    temp = self

    while temp >= 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

        if self == sum:
            return True
        else:
            return False
