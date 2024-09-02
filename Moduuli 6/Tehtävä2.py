import random
def noppa(tahkot):
    return random.randint(1, tahkot)
def ohjelma():
    tahkot = int(input("anna tahkojen määrä: "))
    max = tahkot
    while True:
        silmäluku = noppa(tahkot)
        print("silmäluvun arvo: " + str(silmäluku))
        if silmäluku == max:
            break

ohjelma()