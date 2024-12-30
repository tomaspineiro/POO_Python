""""
## 4. Polimorfismo
**Objetivo:** Usar polimorfismo para tratar objetos de distintas clases de forma uniforme.

### Ejercicio 4.1: Métodos comunes
Crea una lista de objetos que incluyan instancias de `Perro` y `Gato`. Recorre la lista y llama al método `hacer_sonido` de cada objeto.

**Ejemplo de uso:**
```python
animales = [Perro("Rex"), Gato("Luna")]
for animal in animales:
    print(animal.hacer_sonido())
# Salida:
# "Guau"
# "Miau"
```
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


mi_mascotas = (gato("nube"), perro("gox"))

for mascota in mi_mascotas:
    print(mascota.hacer_sonido())