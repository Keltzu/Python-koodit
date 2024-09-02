import math
def y_hinta(ha, hinta):
    pinta_ala = math.pi * (ha / 2) ** 2 / 10000
    return hinta / pinta_ala

halkaisija_a = float(input("anna a pizzan halkaisija: "))
hinta_a = float(input("anna a pizzan hinta: "))
halkaisija_b = float(input("anna b pizzan halkaisija: "))
hinta_b = float(input("anna b pizzan hinta: "))

y_hinta1 = y_hinta(halkaisija_a, hinta_a)
y_hinta2 = y_hinta(halkaisija_b, hinta_b)

if y_hinta1 < y_hinta2:
    print("a pizza hintasuhde parempi.")
else:
    print("b pizza hintasuhde parempi.")