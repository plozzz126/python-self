#игра быки-коровы
# Задание
# Правила игры

# Компьютер задумывает четыре различные цифры из 0,1,2,...9. Игрок делает ходы, чтобы узнать эти цифры и их порядок.

# Каждый ход состоит из четырёх цифр, 0 может стоять на первом месте.

# В ответ компьютер показывает число отгаданных цифр, стоящих на своих местах (число быков) и число отгаданных цифр, стоящих не на своих местах (число коров).

#добавил принцип единой ответственности ну от части. добавил валидацию на вводе 

import random

def input_user():
    while True:
        try:
            herd = int(input("введите кол-во чисел в загадке: "))
            if herd > 10:
                print("более 10 чисел нельзя")
                continue
            elif herd <= 0:
                print("нельзя вводить отрицательные числа и 0")
                continue
            return herd
        except ValueError:
            print("Ошибка, введите целое число")
        
    
herd = input_user()

def gen_num():
    a = ""
    used_num = []
    
    while len(a) < herd:
        num = str(random.randint(0, 9))
       
        if num not in used_num:
            used_num.append(num)
            a += num
    return a

a = gen_num()
print(a)

def validation_num():
    while True:
        num = input(f"введите {herd} чисел/ла: ")

        if not num.isdigit():
            print("Ошибка, введите числа")
            continue
        
        if len(num) < herd:
            print(f"меньше {herd}: ")
            continue
        elif len(num) > herd:
            print(f"больше {herd}: ")
            continue
        return num    

def output(bulls, cow):
    print("число быков: ", bulls)
    print("число коров: ", cow)

def counter():    
    attempts = 0
    while True:
        bulls = 0
        cow = 0
        useless_num = []
        num_bull = []
        num = validation_num()

        for i in range(herd): 
            if num[i] == a[i]:
                bulls += 1
                num_bull.append(i)

        for i in range(herd):
            for j in range(herd):
                if i != j and j not in useless_num and i not in num_bull and num[i] == a[j]:
                    cow += 1
                    useless_num.append(j)
                    break

        attempts += 1
        output(bulls, cow)

        if bulls == herd:
            print(f"победа \n вы угадали число за {attempts} попыток")
            break

counter()





# версия 2.0 
# 1. стадо
# 2. проверка ввода 

# не использовал но в теории мог
# for i in range(herd):
# a = random.randint(0000, sumH - 1)
# print(str(a).zfill(herd))
# print(f"{a:04d}")