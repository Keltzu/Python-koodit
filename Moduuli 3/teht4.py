vuosi = int(input("anna vuosi: "))
karkausvuosi = False

if vuosi % 4 == 0:
    if vuosi % 100 == 0:
        if vuosi % 400 == 0:
            karkausvuosi = True

    else:
        karkausvuosi = True

if karkausvuosi:
    print("karkausvuosi!")

else:
    print("ei karkausvuosi")