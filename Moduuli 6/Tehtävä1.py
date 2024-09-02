import random
def noppa():
    return random.randint(1, 6)

def ohjelma():
    while True:
        silmäluku = noppa()
        print("silmäluvun arvo: " + str(silmäluku))
        if silmäluku == 6:
            break

ohjelma()