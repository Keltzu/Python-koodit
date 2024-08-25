import random

luku = random.randint(1, 10)

while True:
    arvaus = int(input("Arvaa luku väliltä 1-10: "))

    if arvaus < luku:
        print("Liian pieni arvaus")
    elif arvaus > luku:
        print("Liian suuri arvaus")
    else:
        print("Oikein! Luku oli", luku)
        break