luku = int(input("Anna luku: "))

alkuluku = True

for i in range(2,luku):
    if luku % i == 0:
        print(f"{luku} ei ole alkuluku")
        break

else:
    print(f"{luku} on alkuluku")