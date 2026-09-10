#игра быки-коровы
# Задание
# Правила игры

# Компьютер задумывает четыре различные цифры из 0,1,2,...9. Игрок делает ходы, чтобы узнать эти цифры и их порядок.

# Каждый ход состоит из четырёх цифр, 0 может стоять на первом месте.

# В ответ компьютер показывает число отгаданных цифр, стоящих на своих местах (число быков) и число отгаданных цифр, стоящих не на своих местах (число коров).

import random
a = ""

herd = int(input("введите кол-во чисел в загадке: "))
sumH = 1

for i in range(herd):
    sumH *= 10
    a += str(random.randint(0, 9))

print(a)

while True:
    num = input(f"введите {herd} числа: ")
    if len(num) < herd:
        print(f"меньше {herd}: ")
        continue
    elif len(num) > herd:
        print(f"больше {herd}: ")
        continue
    
    bulls = 0
    cow = 0

    for i in range(herd): 
        if num[i] == a[i]:
            bulls += 1
        else:
            continue

    for i in range(herd):
        for j in range(herd):
            if i != j and num[i] == a[j]:
                cow += 1
            else:
                continue

    print("число быков: ", bulls)
    print("число коров: ", cow)

    if bulls == herd:
        print("победа")
        break


# версия 2.0 
# 1. стадо
# 2. проверка ввода 

# не использовал но в теории мог

# for i in range(herd):
# a = random.randint(0000, sumH - 1)
# print(str(a).zfill(herd))
# print(f"{a:04d}")