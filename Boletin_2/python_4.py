"""
## **Ejercicio 4: Manejo de Excepciones Personalizadas**

### **Enunciado:**
Crea un sistema de cuentas bancarias:

1. **Clase `Cuenta`:**
   - Atributos: `titular`, `saldo`.
   - Métodos:
     - `depositar`: añade dinero al saldo.
     - `retirar`: reduce el saldo, pero lanza una excepción personalizada `SaldoInsuficiente` si el saldo es insuficiente.

2. Define la excepción personalizada `SaldoInsuficiente` que incluya un mensaje explicativo.

3. Maneja correctamente las excepciones al intentar retirar dinero.

**Ejemplo:**
```python
cuenta = Cuenta("Juan", 1000)
cuenta.depositar(500)

try:
    cuenta.retirar(2000)
except SaldoInsuficiente as e:
    print(e)
```
 """

class Cuenta():

    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    #getter
    def get_titular(self):
        return self.__titular
    
    def get_saldo(self):
        return self.__saldo
    
    #setter 
    def set_saldo(self, new_seldo):
        self.__saldo = new_seldo
    
    def mostrar(self):

        return f"El titular {self.__titular}, con un saldo {self.__saldo}."

    def deposotar(self, deposito):

        if deposito > 0:
            self.__saldo = self.__saldo + deposito
        

    def retirar(self, retirada ):

        if 0 < retirada <= self.__saldo:

            self.__saldo = self.__saldo - retirada

        else:
            raise SaldoInsuficinete("no puedes hacer retiradas negativas o no tienes saldo suficinete ")


class SaldoInsuficinete(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


cuenta1 = Cuenta("Tomás", 200) 

print(cuenta1.mostrar())

cuenta1.deposotar(150)

print(cuenta1.mostrar())


try:
    
    cuenta1.retirar(700)

except SaldoInsuficinete as e:
    print(e)
print(cuenta1.mostrar())

























































































































