from typing import Literal
""" 
Ejercicio 1: Herencia y Polimorfismo

Enunciado:

Crea un sistema de gestión de vehículos con las siguientes clases:

Clase base Vehiculo:

Atributos: marca, modelo, anio y estado ("en uso" o "disponible").

Método detalles: muestra los datos del vehículo.

Clases hijas:

Coche: agrega un atributo numero_puertas y sobrescribe el método detalles para incluir este dato.

Moto: agrega un atributo tipo ("deportiva" o "urbana") y sobrescribe el método detalles.

Crea una función que reciba una lista de vehículos y muestre los detalles de cada uno utilizando polimorfismo. """

class vehiculo():
    def __init__(self, marca: str, modelo: str, anio: int, estado: Literal ["En uso", "Disponible"] = "Disponible"):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio:int = anio
        self.__estado = estado
    
    #Getter
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo
    
    def get_anio(self):
        return self.__anio
    
    def get_estado(self):
        return self.__estado
    
    #Setter
    def set_marca(self, new_marca):
        self.__marca = new_marca
    
    def set_modelo(self, new_modelo):
        self.__modelo = new_modelo
    
    def set_anio(self, new_anio):
        self.__anio = new_anio

    def set_estado(self, new_estado):
        if new_estado in ["en uso", "disponible"]:
            self.__estado = new_estado
        
        else:

            raise ValueError("No es una opcion valida.")

    def detalles(self):
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__anio}, Estado: {self.__estado}"


class coche(vehiculo):
    
    def __init__(self, marca: str, modelo: str, anio: int, numero_puertas: int, estado: Literal ["En uso", "Disponible"] = "Disponible"):
        super().__init__(marca, modelo, anio, estado)
        self.__numero_puertas = numero_puertas
    
    def get_numero_puertas(self):
        return self.__numero_puertas
    
    def set_numero_puertas(self, new_numero_puertos):
        self.__numero_puertas = new_numero_puertos


    def detalles(self):
        return f"{super().detalles()}, Numero de puertas: {self.__numero_puertas}"

class moto(vehiculo):
    
    def __init__(self, marca: str, modelo: str, anio: int, tipo: Literal ["Deportiva", "Urbana"], estado: Literal ["En uso", "Disponible"] = "Disponible"):
        super().__init__(marca, modelo, anio, estado)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def set_tipo(self, new_tipo):
        if new_tipo in ["Deportiva", "Urbana"]:
            self.__tipo = new_tipo
        else:
            raise ValueError("No es una de las opcines corecta para la varible tipo de la clase moto, que son Deportiva o Urbano. ")
    
    def detalles(self):
        return f"{super().detalles()}, tipo: {self.__tipo}"

vehiculo1 = vehiculo("Mercedes", "clase B", 2009)

print(vehiculo1.detalles())

coche1 = coche("Toyota", "cona", 2023, 5 )

print(coche1.detalles())

moto1 = moto("Yamaja", "mon", 2023, "Urbana" )

print(moto1.detalles())

coche2 = coche("Fiaz", "botella", 2020, 3, "En uso")
moto2 = moto("tubo", "cuerda", 2019, "Deportiva","Disponible" )

vehiculos = [vehiculo1, coche1, moto1, coche2, moto2]
print("......................................")
def mostrar_vehiculos(vehiculos: list):
    
    for veiculo in vehiculos:
        print(" - ",veiculo.detalles())

mostrar_vehiculos([vehiculo1, coche1, moto1, coche2, moto2])