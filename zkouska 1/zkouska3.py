# Definice základní třídy Shape (abstraktní třída)
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

# Třída Rectangle (podtřída třídy Shape)
class Rectangle(Shape):
    def __init__(self, width, height):
        # Inicializace atributů width a height
        self.width = width
        self.height = height

    def area(self):
        # Výpočet plochy obdélníku (šířka × výška)
        return self.width * self.height

# Třída Circle (podtřída třídy Shape)
class Circle(Shape):
    def __init__(self, radius):
        # Inicializace atributu radius
        self.radius = radius

    def area(self):
        # Výpočet plochy kruhu (π × poloměr²)
        return 3.14159 * self.radius ** 2

# Výpočet a výstup výsledků obdélníku a kruhu
rect = Rectangle(4, 5)
print("Area of Rectangle:", rect.area())

circle = Circle(3)
print("Area of Circle:", round(circle.area(), 1))

# Testovací funkce pro ověření správnosti výpočtů
from unittest.mock import patch, MagicMock, mock_open

def test_shapes():
    # Testování třídy Rectangle
    rect = Rectangle(4, 5)
    assert rect.area() == 20

    # Testování třídy Circle
    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3
