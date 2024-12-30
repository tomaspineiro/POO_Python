"""

## 2. Encapsulamiento
**Objetivo:** Proteger los datos dentro de una clase.

### Ejercicio 2.1: Atributos privados
Modifica la clase `Coche` para que los atributos `marca`, `modelo` y `año` sean privados. Esto significa que no deben ser accesibles directamente desde fuera de la clase.

Para lograrlo:
1. Cambia los nombres de los atributos para que comiencen con doble guion bajo (`__`). Por ejemplo: `__marca`, `__modelo`, `__año`.
2. Crea métodos "getter" que permitan acceder a los valores de los atributos privados. Por ejemplo:
   - `get_marca`: devuelve la marca del coche.
   - `get_modelo`: devuelve el modelo del coche.
   - `get_año`: devuelve el año del coche.
3. Crea métodos "setter" que permitan modificar los valores de los atributos privados. Por ejemplo:
   - `set_marca`: actualiza la marca del coche.
   - `set_modelo`: actualiza el modelo del coche.
   - `set_año`: actualiza el año del coche.

**Ejemplo de uso:**
```python
mi_coche = Coche("Honda", "Civic", 2018)
print(mi_coche.get_marca())  # "Honda"
mi_coche.set_año(2022)
print(mi_coche.get_año())  # 2022
print(mi_coche.detalles())  # "Marca: Honda, Modelo: Civic, Año: 2022"
```
**Consejo:**
- El encapsulamiento ayuda a evitar cambios accidentales en los datos desde fuera de la clase y permite controlar cómo se accede y modifica cada atributo.
"""

class coche: 
    
    def __init__(self, marca, modelo, year ):
        self.__marca = marca
        self.__modelo = modelo
        self.__year = year
    
    def  detalles(self):
        return f"Marca:{self.__marca}, Modelo: {self.__modelo} y año {self.__year}"
    
    # Para poder ver los datos de manera individual de cada caracteristica de la clase coche.
    #getter
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo

    def get_year(self):
        return self.__year

    #setter
    def set_modelo(self, new_modelo):
        self.__modelo = new_modelo
    
    def set_marca(self, new_marca):
        self.__marca = new_marca
    
    def set_year(self, new_year):
        self.__year = new_year
    



mi_coche = coche("Mercedes", "clase B", 2009)

print(mi_coche.detalles())

print(mi_coche.get_marca())

mi_coche.set_marca("Toyota")

print(mi_coche.get_marca())

