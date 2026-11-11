# numbers = [1, 2, 3, 4, 5]

# for i in range(len(numbers)):
#     print(f"{numbers[i]} squared is {numbers[i] ** 2}")

def is_odd(numero):
    odd = True
    if numero % 2 == 0:
        odd = False

    else:
        odd = True

    return odd


numbers = [14, 2, 3, 41, 5]

for num in numbers:
    if is_odd(num):
        print(f"{num} is odd")
    else:
        print(f"{num} is even")
