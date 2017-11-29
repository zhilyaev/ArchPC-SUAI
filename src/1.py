import sys


def toHex(v, bits):
    return hex((v + (1 << bits)) % (1 << bits))


def bin_add(*args):
    return bin(sum(int(x, 2) for x in args))[2:]


def toFloat(x):
    if x > 8388607:
        bits = 64
    else:
        bits = 32
    z = '0'
    print('X := ' + str(x))
    if x < 0:
        z = '1'
        x = (-1) * x
    print("Знак = "+z)
    x = bin(x)[2:]
    print('x to bin -> ' + str(x))
    p = len(x)
    print('Порядок -> ' + str(p))
    p = bin(p)[2:]
    print('Порядок to bin -> ' + str(p))
    p = bin_add('10000000', p)
    print('Порядок = ' + str(p))
    m = x[1:]
    print('Мантисса = ' + str(m))
    res = z + p + m
    zero = bits - len(res)
    for i in range(zero):
        res += '0'
    print("=> "+res)
    return hex(int(res, 2))


BIT = 128
V = 6  # Вариант
G = 6  # Группа
print("Вариант: " + str(V))
print("Группа: " + str(G))
S = V + G
x1 = ((-1) ** V) * (S * 3)
x2 = ((-1) ** (V + 1)) * (S + 17)
x3 = ((-1) ** (V + 2)) * ((S + 29) ** 2)
x4 = ((-1) ** (V + 3)) * ((S + 23) ** 2)
x5 = x3 ** 2
x6 = (-1) * (x4 ** 2)
x7 = (-1) * (x5 * (2 ** 28))
x8 = (-1) * (x6 * (2 ** 20))
x9 = (x7 * (2 ** 52)) - 0xc
x = [x1, x2, x3, x4, x5, x6, x7, x8, x9]
print()
print("Пункт A) Десятичные :")
for i in x:
    print(i)
print()
print("Пункт Б) Перевод в HEX :")
for i in x:
    print(toHex(i, BIT))
print()
print("Пункт Г) Адресса данных :")
for i in range(len(x)):
    it = (G * V) + 10 * i
    print(str(it) + " => " + toHex(it, BIT))  # toHex() can be replaced with hex()
print()
print("Пункт Д) Адресса данных :")
for i in range(len(x)):
    it = V + 100 + (i * 10)
    print(str(it) + " => " + toHex(it, BIT))  # toHex() can be replaced with hex()
print()
print("E) Начальный адрес размещения:")
print(V * 10 + 200)
print()
print("Ж) Начальный адрес размещения:")
print(V * G + 230)
print()
print("З) Начальный адрес размещения:")
print(V * G + 300)
print()
print("В системе с плавающей запятой")
for i in x:
    print(toFloat(i))
    print('=============================')
