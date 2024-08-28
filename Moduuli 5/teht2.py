luvut = []

while True:
    s = input("Anna luku: ")
    if s == "":
        break
    luvut.append(int(s))

luvut.sort(reverse=True)

print("Viisi suurinta lukua:")
for luku in luvut[:5]:
    print(luku)