# napiste funkci, ktera podle typu "+"", "-", "*", "/" provede operaci a vrati vysledek

def operace(typ, a, b):
    matematicka_operace = None
    if typ == "+":
        matematicka_operace = a + b
    elif typ == "-":
        matematicka_operace = a - b
    elif typ == "*":
        matematicka_operace = a * b
    elif typ == "/":
        if b != 0:  # Ošetření dělení nulou
            matematicka_operace = a / b
        else:
            return "Chyba: dělení nulou není povoleno"
    else:
        return "Neplatný typ operace"
    return matematicka_operace

if __name__ == "__main__":
    print(operace("+", 1, 2))  # 3
    print(operace("-", 2, 1))  # 1
    print(operace("*", 0, 5))  # 0
    print(operace("/", 4, 2))  # 2
    print(operace("/", 4, 0))  # Chyba: dělení nulou není povoleno
    print(operace("^", 2, 3))  # Neplatný typ operace
