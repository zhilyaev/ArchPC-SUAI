import sys


def toHex(v, bits):
    return hex((v + (1 << bits)) % (1 << bits))


BIT = 128
V = int(sys.argv[1])  # Вариант
G = int(sys.argv[2])  # Группа
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
