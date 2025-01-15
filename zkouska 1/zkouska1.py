def process_strings(strings):
    # Inicializace prázdného seznamu pro ukládání výsledků
    result = []
    # Procházení každého řetězce v seznamu
    for string in strings:
        # Pokud je řetězec "STOP", ukonči zpracování seznamu
        if string == "STOP":
            break
        # Pokud má řetězec více než 3 znaky, převeď ho na velká písmena a přidej do výsledků
        if len(string) > 3:
            result.append(string.upper())
    # Vrácení seznamu výsledků
    return result

# Pytest testy pro Příklad 2
def test_process_strings():
    # Test: Zpracování seznamu s "STOP" na druhém místě
    print(process_strings(["abc", "abcd", "STOP", "efgh"]))  # Očekávaný výstup: ["ABCD"]
    # Test: Zpracování seznamu s "STOP" uprostřed seznamu
    print(process_strings(["hello", "world", "STOP", "python"]))  # Očekávaný výstup: ["HELLO", "WORLD"]
    # Test: Zpracování seznamu bez řetězců delších než 3 znaky
    print(process_strings(["hi", "ok", "go"]))  # Očekávaný výstup: []
    # Test: Zpracování seznamu bez "STOP" a s více platnými řetězci
    print(process_strings(["code", "test", "debug"]))  # Očekávaný výstup: ["CODE", "TEST", "DEBUG"]

test_process_strings()
