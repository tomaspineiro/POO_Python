from typing import Literal
"""
## **Ejercicio 5: Proyecto Final - Sistema de Reserva de Habitaciones**

### **Enunciado:**
Crea un sistema para gestionar las reservas de un hotel con las siguientes clases:

1. **Clase `Habitacion`:**
   - Atributos: `numero`, `tipo` ("individual", "doble", "suite"), `precio` y `estado` ("disponible" o "ocupada").
   - Método `reservar`: cambia el estado a "ocupada".
   - Método `liberar`: cambia el estado a "disponible".

2. **Clase `Cliente`:**
   - Atributos: `nombre`, `dni`, lista de habitaciones reservadas.
   - Método para mostrar las habitaciones reservadas.

3. **Clase `Hotel`:**
   - Atributos: nombre del hotel, lista de habitaciones.
   - Métodos:
     - `mostrar_habitaciones_disponibles`: muestra todas las habitaciones libres.
     - `realizar_reserva`: permite a un cliente reservar una habitación.
     - `cancelar_reserva`: libera una habitación reservada.

**Ejemplo:**
```python
hotel = Hotel("Gran Hotel")
habitacion1 = Habitacion(101, "doble", 100)
habitacion2 = Habitacion(102, "suite", 200)
hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)

cliente = Cliente("Ana", "12345678A")
hotel.realizar_reserva(cliente, 101)
cliente.mostrar_reservas()
hotel.mostrar_habitaciones_disponibles()
```
"""

class Habitacion():
    
    def __init__(self, numero, precio, tipo: Literal["Individual", "Doble", "Suite"] = "Individual",  estado: Literal["Disponible", "Ocupado"] = "Disponible"):
        self.__numero = numero
        self.__precio = precio
        self.__tipo = tipo
        self.__estado = estado

    #getter
    def get_numero(self):
        return self.__numero
    
    def get_precio(self):
        return self.__precio
    
    def get_tipo(self):
        return self.__tipo
    
    def get_estado(self):
        return self.__estado
    
    #setter
    def set_estado(self, new_estado: Literal["Disponible", "Ocupado"]):
        self.__estado = new_estado

    def mostrar(self):
        return f"   - Numero: {str(self.__numero)}, Precio: {str(self.__precio / 100)}, Tipo: {self.__tipo}, Estado: {self.__estado}."
    

    def reservar(self):
        self.set_estado("Ocupado")

    def liberar(self):
        self.set_estado("Disponible")

class Cliente():
    def __init__(self, nombre, dni):
        self.__nombre = nombre
        self.__dni = dni
        self.__list_habitaciones_reservadas = []

    #getter
    def get_nombre(self):
        return self.__nombre
    
    def get_dni(self):
        return self.__dni
    
    def get_habitacion_reservadas(self):
        return self.__list_habitaciones_reservadas
    
    def mostrar(self):
        print(f"cliente: {self.__nombre}, Dni: {self.__dni}")
        if len(self.__list_habitaciones_reservadas) > 0:
            print("Habitacion:")
            for habitacion in self.__list_habitaciones_reservadas:
                print(habitacion.mostrar())
        else: 
            print("Habitaciones: 0")

class Hotel():

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__list_cliente = []
        self.__list_habitacion = []


    def new_cliente(self, new_cliente):
        self.__list_cliente.append(new_cliente)

    def new_room(self, new_room):
        self.__list_habitacion.append(new_room)

    def reserva(self, habitacion):
        habitacion.reservar()

    def Cancelar_reserva(self, habitacion):
        habitacion.liberar()

    def room_free(self):
        if len(self.__list_habitacion) > 0:
            for room in self.__list_habitacion:
                if room.get_estado() == "Disponible":
                    print(room.mostrar())


hab1 = Habitacion(112, 500)
hab2 = Habitacion(113, 500)
hab3 = Habitacion(114, 500, "Doble", "Ocupado")
hab4 = Habitacion(115, 500)

hotel1 = Hotel("DeerPark")

hotel1.new_room(hab1)
hotel1.new_room(hab2)
hotel1.new_room(hab3)
hotel1.new_room(hab4)



hotel1.room_free()

