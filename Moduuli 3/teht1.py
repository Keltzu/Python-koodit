pituus = float(input("anna pituus: "))
if pituus < 37:
    puuttuu = 37 - pituus
    print("pituutta puuttuu " + str(37-pituus) + "cm")

else:
    print("oikean mittainen!")