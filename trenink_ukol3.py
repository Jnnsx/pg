def je_prvocislo(cislo):
    """
    Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False.

    Prvocislo je takove cislo vetsi nez 1, ktere neni delitelne zadnym jinym cislem jenom 1 a samo sebou.
    """
    if cislo <= 1:
        return False
    # Hledáme dělitele pouze do odmocniny čísla bez použití knihovny
    delitel_limit = 1
    while delitel_limit * delitel_limit <= cislo:
        delitel_limit += 1
    for i in range(2, delitel_limit):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    """
    Funkce spocita vsechna prvocisla v rozsahu 1 az maximum a vrati je jako seznam.
    """
    return [x for x in range(2, maximum + 1) if je_prvocislo(x)]

if __name__ == "__main__":
    try:
        cislo = int(input("Zadej maximum: "))
        prvocisla = vrat_prvocisla(cislo)
        print(f"Prvocisla od 1 do {cislo}: {prvocisla}")
    except ValueError:
        print("Zadané číslo musí být celé číslo.")
