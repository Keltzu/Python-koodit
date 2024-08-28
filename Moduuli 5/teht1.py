import random
arpa = int(input("Anna kuution lukumäärä: "))

summa = 0

for i in range(arpa):
    heitto = random.randint(1, 6)
    summa += heitto

print("summa on: " + str(summa))