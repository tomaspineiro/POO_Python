from abc import ABC, abstractmethod
from math import pi

""" 
## **Ejercicio 2: Abstracción con Clases Abstractas**

### **Enunciado:**
Usa el módulo `abc` para crear una clase abstracta `Figura` con:

1. Un método abstracto `calcular_area`.
2. Un método abstracto `calcular_perimetro`.

Luego, crea las clases:
- **`Rectangulo`** con atributos `base` y `altura`.
- **`Circulo`** con atributo `radio`.

Ambas clases deben implementar los métodos abstractos. Además, incluye un método `mostrar_info` que imprima área y perímetro.

**Ejemplo:**
```python
rectangulo = Rectangulo(5, 10)
circulo = Circulo(7)

rectangulo.mostrar_info()
circulo.mostrar_info()
```
"""

class figura(ABC): 

    @abstractmethod
    def calcular_area(self):
        """esto es para calcular la area de las figuras """
        pass

    @abstractmethod
    def calcular_perimetro(self):
        """Esto es para calcular el perimetro de las figuras """
        pass

    @abstractmethod
    def datos(self):
        """Esto es para mostrar los datos de cada figura"""

    
    def detalles(self):
        return f"Figura: {self.datos()} \n · Area: {self.calcular_area()} \n · Perimetro: {self.calcular_perimetro()}"
    

class circulo(figura):

    def __init__(self, radio):
        self.__radio = radio

    def calcular_area(self):
        return pi * self.__radio ** 2
    
    def calcular_perimetro(self):
        return pi * self.__radio * 2

    def datos(self):
        return f"Circulo de  radio {self.__radio}"

class rectangulo(figura):

    def __init__(self, lado1, lado2):
        self.__lado1 = lado1
        self.__lado2 = lado2
        
    def calcular_area(self):
        return self.__lado1 * self.__lado2

    def calcular_perimetro(self):
        return 2 * (self.__lado1 + self.__lado2)
    
    def datos(self):
        return f"Rectangulo con lados de {self.__lado1} y {self.__lado2}"


circulo1 = circulo(3)
rectangulo1 = rectangulo(2,4)

print(circulo1.detalles())
print("_" * 24 + "\n")
print(rectangulo1.detalles())