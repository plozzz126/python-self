# написать свой псевдо рандомайзер, сделать генерацию пароля определённой длины

import random

chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.,?!'&@"

def genp():
    count = int(input("введите кол-во символов в пароле: "))
    pass_ = ""
    for _ in range(count):
        x = random.randint(0, len(chars) -1)
        pass_  += chars[x]
    
    print(pass_)

genp()


