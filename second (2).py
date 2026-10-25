def cislo_text(cislo):
    # Prevede cislo od 0 do 100 na text.
    cislo = int(cislo)

    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    do_devatenacti = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]

    if cislo < 0 or cislo > 100:
        return "Zadej číslo od 0 do 100"

    if cislo < 10:
        return jednotky[cislo]
    elif cislo < 20:
        return do_devatenacti[cislo - 10]
    elif cislo == 100:
        return "sto"
    else:
        desitka = cislo // 10
        jednotka = cislo % 10

        if jednotka == 0:
            return desitky[desitka]
        else:
            return desitky[desitka] + " " + jednotky[jednotka]


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
