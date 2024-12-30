""" 
### Ejercicio 3.1: Herencia básica
Crea una clase base llamada `Animal` con los siguientes atributos y métodos:
- `nombre` (cadena de texto)
- Método `hacer_sonido()` que devuelve "Sonido genérico".

Luego, crea dos clases derivadas:
1. `Perro`, que sobrescribe el método `hacer_sonido` para devolver "Guau".
2. `Gato`, que sobrescribe el método `hacer_sonido` para devolver "Miau".

**Ejemplo de uso:**
```python
mi_perro = Perro("Rex")
print(mi_perro.hacer_sonido())  # "Guau"

mi_gato = Gato("Luna")
print(mi_gato.hacer_sonido())  # "Miau"
```

---
 """

class animales():

    def __init__(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
        
    def hacer_sonido(self):
        return "Sonido genérico"

    
class gato(animales):

   def hacer_sonido(self):
        return "Miau"

class perro(animales):
    
    def hacer_sonido(self):
        return "Guau"


mi_gato = gato("nube")
mi_perro = perro("gox")


print(mi_gato.hacer_sonido())
print(mi_perro.hacer_sonido())