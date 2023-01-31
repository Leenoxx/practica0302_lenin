# Crear una Clase Producto con los siguientes atributos:
#  - código
#  - nombre
#  - precio
# Crea su constructor, getter y setter y una función llamada calcular_total,
# donde le pasaremos unas unidades y nos debe calcular el precio final.
class Producto:

    # Inicializador que crea los atributos necesarios para el objeto
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    @property   # Getter =  función que DEVUELVE el valor que pedimos
    def codigo(self):
        return self.__codigo

    @codigo.setter   # Setter = función que MODIFICA el valor que damos
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

    def __str__(self):   # Función que devuelve una descripción del objeto.
        return "Código: " + str(self.__codigo) + " || Nombre: " + self.__nombre + " || Precio: " + str(self.__precio)


p1 = Producto(1, "Patata", 5)
p2 = Producto(2, "Huevos", 4)
p3 = Producto(3, "Pan", 2)

print(p1)
print(p2)
print(p3)

print(p1.calcular_total(10))
print(p2.calcular_total(10))
print(p3.calcular_total(10))
