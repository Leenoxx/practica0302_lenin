# Añadir una clase Pedido que tiene como atributos:
#     - lista de productos
#     - lista de cantidades
# Añade las siguiente funcionalidad:
#     - total_pedido: muestra el precio final del pedido
#     - mostrar_productos: muestra los productos del pedido
class Producto:

    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, new_codigo):
        self.__codigo = new_codigo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, new_precio):
        self.__precio = new_precio

    def calcular_total(self, cantidad):
        return self.__precio * cantidad

    def __str__(self):
        return "Código: " + str(self.__codigo) + " || Nombre: " + self.__nombre + " || Precio: " + str(self.__precio)


class Pedido:

    def __init__(self, productos, cantidades):  # Inicializador para el molde Pedido
        self.__productos = productos
        self.__cantidades = cantidades

    def total_pedido(self):  # Función que calcula el total del pedido, usando los valores del init
        total = 0
        # (prod, cant) son los valores que recorren las dos listas con ayuda de zip
        for (prod, cant) in zip(self.__productos, self.__cantidades):
            total = total + prod.calcular_total(cant)
            # del valor prod de la primera lista llamamos a la funcion
            # de la clase Producto con el valor cant de la segunda lista

        return total

    def mostrar_pedido(self):  # Función que muestra el pedido
        for (prod, cant) in zip(self.__productos, self.__cantidades):
            print("Producto =>", prod.nombre, "|| Cantidades", cant)
            # con el valor prod llamamos a la funcion de la clase Producto "nombre"
            # mostrando unicamente el nombre del producto y de la lista de cantidades
            # imprimimos el valor.


p1 = Producto(1, "Patata", 5)
p2 = Producto(2, "Huevos", 4)
p3 = Producto(3, "Pan", 2)

print(p1)
print(p2)
print(p3)

print(p1.calcular_total(10))
print(p2.calcular_total(10))
print(p3.calcular_total(10))

lista_productos = [p1, p2, p3]
lista_cantidades = [5, 10, 4]

pedido = Pedido(lista_productos, lista_cantidades)
print("Total pedido =", str(pedido.total_pedido()))
pedido.mostrar_pedido()
