from random import randint

""" ## **Ejercicio 3: Relaciones entre Clases**

### **Enunciado:**
Diseña un sistema de gestión de una tienda:

1. **Clase `Producto`:**
   - Atributos: `nombre`, `precio`, `stock`.
   - Métodos para aumentar y disminuir el stock.

2. **Clase `Carrito`:**
   - Atributos: lista de productos y cantidades.
   - Métodos:
     - `agregar_producto`: recibe un producto y una cantidad.
     - `eliminar_producto`: elimina un producto del carrito.
     - `calcular_total`: devuelve el costo total.

3. **Clase `Tienda`:**
   - Atributos: nombre de la tienda y lista de productos disponibles.
   - Métodos para mostrar los productos disponibles y procesar compras.

**Ejemplo:**
```python
producto1 = Producto("Manzana", 0.5, 50)
producto2 = Producto("Pan", 1.0, 20)

carrito = Carrito()
carrito.agregar_producto(producto1, 5)
carrito.agregar_producto(producto2, 2)
print(carrito.calcular_total())
```
"""
class Product(): 
   
   def __init__(self, nombre, precio:int, stock:int):
      self.__nombre = nombre
      self.__precio = precio
      self.__stock = stock

   #getter
   def get_nombre(self):
      return self.__nombre

   def get_precio(self):
      return self.__precio

   def get_stock(self):
      return self.__stock

   #setter
   def set_nombre(self, new_nombre):
      self.__nombre = new_nombre

   def set_precio(self, new_precio:int):
      self.__precio = new_precio

   def __set_stock(self, new_stock:int):
      self.__stock = new_stock
      
   #incremetno de stock
   def increment_stock(self, more_stock:int):
      if more_stock >= 0: 
         new_stock = self.__stock + more_stock
         self.__set_stock(new_stock)
      else: 
         raise ValueError("tiene que ser un numero entero positivo ")
      
   def decrement_stock(self, less_stock:int): 
      
      if 0 < less_stock <= self.__stock:
         new_stock = self.__stock - less_stock
         self.__set_stock(new_stock)
      else:
         raise ValueError("la reduccion de stock tiene qu estar entre 0 y el stock disponible")
      
   def mostrar(self):
      precio = self.__precio / 100
      return f"Nombre: {self.__nombre}, Precio:  {precio}€, stock: {self.__stock}"

class trollery():
   def __init__(self):
      self.__list_products = []
   
   def get_list_products(self):
      return self.__list_products
   
   def mostrar(self):
      
      if len(self.__list_products) > 0:
      
         for product in self.__list_products:
      
            print(f"Producto: {product[0].mostrar()}, Cantidad:  {product[1]}" )

   def add_product(self, product_name:object, amount:int, shop_1):
      
      products = shop_1.get_products()
      
      for product in products:
         
         if product_name == product.get_nombre() and 0 < product.get_stock() >= amount:

            self.__list_products.append([product, amount])

        
   def delete_product(self, producto_name):

      if len(self.__list_products) > 0:

         products_to_remove = [product for product in self.__list_products if producto_name == product[0].get_nombre()]
    
         for product in products_to_remove:

             self.__list_products.remove(product)


   def calculate_all(self):
      all_cost = 0

      if len(self.__list_products) > 0:

         for product in self.__list_products:
            
            all_cost = all_cost + product[0].get_precio() * product[1]
      
      return all_cost / 100
      
      

class shop():

   def __init__(self, name):
      self.__name = name
      self.__products = []
   
   def get_products(self):
      return self.__products

   def add_product(self, product):
      self.__products.append(product)
   
   def mostrar(self):
      print("Tenemos estos productos disponibles en la tienda:")

      for product in self.__products:
         if (product.get_stock()) > 0:
            print("- " +  product.mostrar())
      

   def procesar_compra(self, trollery_list):
      
      if len(trollery_list) > 0:
         for product in trollery_list:
            product[0].decrement_stock(product[1])

         

      

def crear_lista_de_productos_shop(cantidad, shop):

   for number in range(cantidad):

      name = f"Producto{str(number)}"
      centimos = randint(1,999)
      stock = randint(1,50)
      #print(f"{name} {str(centimos)} {str(stock)}")
      producto = Product(name, centimos, stock)
      shop.add_product(producto)


shop1 = shop("Pepe")


crear_lista_de_productos_shop(15, shop1)


#shop1.mostrar() 
trollery1 = trollery()
trollery1.add_product("Producto13", 1, shop1)
trollery1.add_product("Producto12", 1, shop1)
trollery1.add_product("Producto11", 1, shop1)
trollery1.add_product("Producto10", 1, shop1)
shop1.mostrar() 

trollery1.delete_product("Producto12")
trollery1.mostrar() 

print(trollery1.calculate_all())


shop1.procesar_compra(trollery1.get_list_products())

shop1.mostrar() 

list_product = shop1.get_products()



#print(list_product[0].get_nombre ())

#Carrito. add_product()

