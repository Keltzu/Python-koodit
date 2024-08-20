leiviskat = int(input("Anna leivisköiden määrä: "))
naulat = int(input("Anna naulojen määrä: "))
luodit = int(input("Anna luotien määrä: "))

leiviska_grammoina = leiviskat * 20 * 32 * 13.3
naula_grammoina = naulat * 32 * 13.3
luoti_grammoina = luodit * 13.3


kokonaisgrammat = leiviska_grammoina + naula_grammoina + luoti_grammoina
kilogrammat = int(kokonaisgrammat // 1000)
jäljellä_olevat_grammat = kokonaisgrammat % 1000

print(f"Massa on {kilogrammat} kg ja {jäljellä_olevat_grammat:.1f} g.")