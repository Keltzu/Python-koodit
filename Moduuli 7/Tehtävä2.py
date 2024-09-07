nimet = set()

while True:
    nimi = input("Anna nimi: ")

    if nimi == "":
        break

if nimi in nimet:
    print("Jo syötetty nimi")
else:
    print("uusi nimi")
    nimet.add(nimi)

print("syötetyt nimet:")
for nimi in nimet:
    print(nimi)