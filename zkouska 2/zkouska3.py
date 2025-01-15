# Definujeme základní třídu Osoba, která bude sloužit jako rodičovská třída
class Osoba:
    # Konstruktor třídy Osoba, který inicializuje atributy jmeno a vek
    def __init__(self, jmeno, vek) -> None:
        self.jmeno = jmeno  # Atribut jmeno obsahuje jméno osoby
        self.vek = vek      # Atribut vek obsahuje věk osoby

    # Metoda __str__ určuje, jak se instance třídy Osoba zobrazí jako řetězec
    def __str__(self) -> str:
        return f"Osoba(jmeno={self.jmeno}, vek={self.vek})"

# Definujeme třídu Student, která dědí z třídy Osoba
class Student(Osoba):
    # Konstruktor třídy Student, který rozšiřuje konstruktor třídy Osoba
    def __init__(self, jmeno, vek, rocnik) -> None:
        super().__init__(jmeno, vek)  # Voláme konstruktor rodičovské třídy Osoba
        self.rocnik = rocnik          # Atribut rocnik specifikuje ročník studenta
    
    # Metoda __str__ přetěžuje metodu z třídy Osoba a mění způsob zobrazení
    def __str__(self) -> str:
        return f"Student {self.jmeno} studuje {self.rocnik} rocnik"

# Definujeme třídu Ucitel, která také dědí z třídy Osoba
class Ucitel(Osoba):
    # Konstruktor třídy Ucitel, který rozšiřuje konstruktor třídy Osoba
    def __init__(self, jmeno, vek, obor) -> None:
        super().__init__(jmeno, vek)  # Voláme konstruktor rodičovské třídy Osoba
        self.obor = obor              # Atribut obor specifikuje vyučovaný obor
    
    # Metoda __str__ přetěžuje metodu z třídy Osoba a mění způsob zobrazení
    def __str__(self) -> str:
        return f"Ucitel {self.jmeno} uci obor {self.obor}"

# Hlavní část programu
if __name__ == "__main__":
    # Vytvoření instance třídy Student s konkrétními údaji
    student1 = Student("Adam", 20, 2)  # Student jménem Adam, 20 let, 2. ročník
    student2 = Student("Eva", 19, 1)   # Studentka jménem Eva, 19 let, 1. ročník
    # Vytvoření instance třídy Ucitel s konkrétními údaji
    ucitel = Ucitel("Tomas", 40, "IT") # Učitel jménem Tomas, 40 let, obor IT

    # Výpis informací o studentovi Adamovi
    print(student1)  # Zavolá metodu __str__ pro student1
    # Výpis informací o studentce Evě
    print(student2)  # Zavolá metodu __str__ pro student2
    # Výpis informací o učiteli Tomasovi
    print(ucitel)    # Zavolá metodu __str__ pro ucitel
