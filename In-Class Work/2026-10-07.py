numbers = [1, 2, 3, 4, 5]


def is_odd(value: int):
    odd = True
    if value % 2 == 0:
        odd = False
    else:
        odd = True

    return odd


for number in numbers:
    if is_odd(number):
        print(f"{number} is odd.")
    else:
        print(f"{number} is even.")
