#игра угадай число

import random
print("угадай число от 1 до 100")

x = random.randint(1, 100)

while True:
    num = int(input("Введите ваше число: "))
    if num == x:
        print("вы угадали ")
        break
    else:
        print("не угадал")