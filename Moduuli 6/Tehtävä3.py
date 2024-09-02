while True:
    gallon = float(input("Anna gallona summa (- lopettaa): "))
    if gallon < 0:
        print("Ohjelma loppuu")
        break
    litra = gallon * 3.785
    print(str(gallon) + " gallonaa on " + str(litra) + " litraa")