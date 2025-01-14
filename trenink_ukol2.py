def cislo_text(cislo):
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    zvlastni = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]

    cislo = int(cislo)  # Převod vstupu na celé číslo
    if cislo < 10:  # Čísla od 0 do 9
        return jednotky[cislo]
    elif 10 <= cislo < 20:  # Čísla od 10 do 19
        return zvlastni[cislo - 10]
    elif 20 <= cislo < 100:  # Čísla od 20 do 99
        desitka = cislo // 10  # Výpočet desítek
        jednotka = cislo % 10  # Výpočet jednotek
        if jednotka == 0:  # Pokud není zbytek, vrátíme pouze desítky
            return desitky[desitka]
        else:  # Jinak vrátíme kombinaci desítek a jednotek
            return f"{desitky[desitka]} {jednotky[jednotka]}"
    elif cislo == 100:  # Speciální případ pro 100
        return "sto"
    else:  # Pokud je číslo mimo rozsah
        return "Číslo mimo rozsah (0-100)"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
