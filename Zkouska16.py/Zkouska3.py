
# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte dvě podtřídy třídy `Shape`: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`, která spočítá plochu obdelníku (zaokrouhlenou na 1 desetinné místo).
# - `Circle` má atribut `radius` a implementuje metodu `area`, která spočítá plochu kruhu (zaokrouhlenou na 1 desetinné místo).
# - ve třídě `Circle` navíc implementujte metodu `__str__`, která vrátí řetězec ve tvaru `{self.shape_name} with a radius of {self.radius} has an area of {self.area}`.


class Shape():#rodicovska trida shape

    def __init__(self, shape_name=None): #nastavuje atribut shape_name
        self.shape_name = shape_name #pokud nebude prirazen nazev zustava none
    
    def __str__(self):  #urcuje jak se trida bude chovat pri prevodu na retezec
        return f'{self.shape_name} shape with area {self.area()}'

    def area(self): #slouzi jako vychozi metoda pro vypocet plochy
        return 0.0



class Rectangle(Shape): #trida obdelnik
    def __init__(self, width, height):
        super().__init__(shape_name="Rectangle")  # Nastavíme název tvaru
        self.width = width  # Šířka obdélníku
        self.height = height  # Výška obdélníku

    def area(self):
        return round(self.width * self.height, 1)  # Výpočet a zaokrouhlení plochy obdélníku


class Circle(Shape): #trida kruh
    def __init__(self, radius):
        super().__init__(shape_name="Circle")  # Nastavíme název tvaru
        self.radius = radius  # Poloměr kruhu

    def area(self):
        return round(3.14159 * self.radius ** 2, 1)  # Výpočet a zaokrouhlení plochy kruhu

    def __str__(self):
        return f"{self.shape_name} with a radius of {self.radius} has an area of {self.area()}"



from unittest.mock import patch, MagicMock, mock_open


if __name__ == "__main__":
    shape = Shape()
    print(shape)
    rect = Rectangle(4, 5)
    print(rect)
    circle = Circle(3)
    print(circle)
