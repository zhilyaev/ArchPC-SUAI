def toHex(v, bits):
    return hex((v + (1 << bits)) % (1 << bits))


V = 4  # Вариант
G = 2  # Группа
S = V + G
x1 = (-1 ** V) * (S * 3)
x2 = (-1 ** (V + 1)) * (S + 17)
x3 = (-1 ** (V + 2)) * ((S + 29) ** 2)
x4 = (-1 ** (V + 3)) * ((S + 23) ** 2)
x5 = x3 ** 2
x6 = -1 * (x4 ** 2)
x7 = -1 * (x5 * (2 ** 28))
x8 = -1 * (x6 * (2 ** 20))
x9 = (x7 * (2 ** 52)) - 0xc
x = [x1, x2, x3, x4, x5, x6, x7, x8, x9]
print("DECIMAL :")
for i in x:
    print(i)
print()
print("HEX :")
for i in x:
    print(toHex(i, 128))
print()
print("ADDRESS :")
for i in range(len(x)):
    print(S + i * 10)
