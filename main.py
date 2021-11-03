import random


def genPassword():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    symb = "[]{}#()*;.-"
    length = 9
    all = lower + upper + num + symb
    password = "".join(random.sample(all, length))
    print("Your random password is : ", password)

genPassword()
