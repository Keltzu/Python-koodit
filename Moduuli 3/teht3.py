sukupuoli = input("kerro sukupuoli (M/N): ")
hemo_arvo = float(input("anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "M":
    if hemo_arvo < 134:
        print("hemoglobiiniarvo liian alhainen")
    elif hemo_arvo > 195:
        print("hemoglobiiniarvo liian korkea")
    else:
        print("hemoglobiiniarvo on normaali");


elif sukupuoli == "N":
    if hemo_arvo < 117:
        print("hemoglobiiniarvo liian alhainen")
    elif hemo_arvo > 175:
        print("hemoglobiiniarvo liian korkea")
    else:
        print("hemoglobiiniarvo on normaali");

else:
    print("virheellinen sukupuoli.")