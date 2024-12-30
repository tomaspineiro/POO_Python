""" ## 5. Proyecto Final
**Objetivo:** Aplicar los conceptos aprendidos.

### Ejercicio 5.1: Sistema de gestión de biblioteca
Crea un sistema de gestión de biblioteca con las siguientes clases:
1. `Libro`: atributos como `titulo`, `autor`, y `estado` ("disponible" o "prestado").
2. `Usuario`: atributos como `nombre` y una lista de libros prestados.
3. Métodos para prestar y devolver libros, y para mostrar el estado actual de la biblioteca.

**Ejemplo de uso:**
```python
libro1 = Libro("1984", "George Orwell")
usuario1 = Usuario("Ana")

usuario1.prestar_libro(libro1)
print(libro1.estado)  # "prestado"
usuario1.devolver_libro(libro1)
print(libro1.estado)  # "disponible"
```
 """

class libro():
    
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__estado = "Disponible"

    
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_estado(self):
        return self.__estado
    
    def set_titulo(self, new_titulo):
        self.__titulo = new_titulo

    
    def set_autor(self, new_autor):
        self.__autor = new_autor

    def set_estado(self, new_estado):
        if new_estado in ["disponible", "prestado"]:
            self.__estado = new_estado
        else:
            return ValueError("opcion Incorrecta")
    
    def descripcion(self):
        return f"Titulo: {self.__titulo}, Autor: {self.__autor}, Estado: {self.__estado}"




class usuario():
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libros = []

    def get_nombre(self):
        return self.__nombre

    def get_usuario(self): 
        print(f"El usuario: {self.__nombre}")
        print("Tiene estos libros prestaos:")
        for libro in self.__libros:
            print(libro.descripcion())

    def prestar(self, libro_prestado):
        if libro_prestado.get_estado() == "prestado":
            print("el libro ya esta prestado.")
            return
            
        self.__libros.append(libro_prestado)
        libro_prestado.set_estado("prestado")

    def devolver(self, libro_devolver):
        if not self.__libros in libro_devolver:
            print(f"EL usuario {self.__nombre}, no tiene el libro ")
            return

        self.__libros.remove(libro_devolver)
        libro_devolver.set_estado("Disponible")


        
    
    
libro1 = libro("1984", "George Orwell")

print(libro1.descripcion())

user1 = usuario("tomas")

user1.prestar(libro1)

print("....................")

user1.get_usuario()

user1.devolver(libro1)

print("....................")
user1.get_usuario()


