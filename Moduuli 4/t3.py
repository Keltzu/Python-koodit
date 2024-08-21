minluku = None
maxluku = None

while True:
    s = input("Anna luku (tyhjällä merkkijonolla lopetetaan): ")

    if s == "":

        break

    try:
        luku = float(s)
    except ValueError:

        print("Virheellinen syöte. Anna kelvollinen numero.")
        continue

    if minluku is None or luku < minluku:
        minluku = luku
    if maxluku is None or luku > maxluku:
        maxluku = luku

if minluku is not None and maxluku is not None:
    print("Pienin luku on " + str(minluku))
    print("Suurin luku on " + str(maxluku))
else:
    print("Ei syötettyjä lukuja.")