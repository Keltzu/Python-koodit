def summa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

luvut = [1, 2, 3, 4, 5]
tulo = summa(luvut)
print("lukujen summa on " + str(tulo))
