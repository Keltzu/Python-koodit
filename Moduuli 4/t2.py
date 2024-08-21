tuuma = 2.54
while True:
    inches = float(input("Kerro pituus tuumina: "))
    if inches < 0:
        break
    senttimetrit = inches * tuuma
    tulos = "Pituus senttimetreinä on " + str(round(senttimetrit, 2)) + " cm."
    print(tulos)