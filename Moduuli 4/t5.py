o_tunnus = "python"
o_salasana = "rules"

yritys = 0
m_yritys = 5

while yritys < m_yritys:
    tunnus = input("käyttäjätunnus: ")
    salasana = input("salasana: ")

    if tunnus == o_tunnus and salasana == o_salasana:
        print("Tervetuloa")
        break
    else:
        yritys += 1
        print("väärä tunnus tai salasana")

if yritys == m_yritys:
    print("Pääsy evätty")