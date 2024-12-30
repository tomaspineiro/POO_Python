""" 1. Clases y Objetos

    Objetivo: Crear y manipular clases y objetos.

    Ejercicio 1.1: Tu primera clase

    Crea una clase llamada Coche que tenga los siguientes atributos:

    marca (cadena de texto)

    modelo (cadena de texto)

    año (entero)

    Incluye un método llamado detalles que devuelva una cadena con la información del coche. """
""" Ejercicio 1.2: Modificar atributos

Añade un método llamado actualizar_modelo que permita cambiar el modelo del coche. """

class coche: 
    
    def __init__(self, marca, modelo, year ):
        self.marca = marca
        self.modelo = modelo
        self.year = year
    
    def  detalles(self):
        return f"Marca:{self.marca}, Modelo: {self.modelo} y año {self.year}"
    
    def modificar_modelo(self, new_modelo):
        self.modelo = new_modelo


    
Mi_coche = coche("Mercedes", "clase B", 2009 )

print(Mi_coche.detalles())

Mi_coche.modificar_modelo("clase A")

print(Mi_coche.detalles())

Mi_coche.modelo = "clase C"

print(Mi_coche.detalles())
