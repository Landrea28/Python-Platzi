class Vehiculo():
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.disponible = True

    def vender(self):
        if self.disponible:
            print(f"El {self.marca} {self.modelo} del año {self.año} ha sido vendido.")
            self.disponible = False
        else:
            print(f"Lo siento, el {self.marca} {self.modelo} del año {self.año} no está disponible para la venta.")

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")

    def disponibilidad(self):
        return self.disponible

class User():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.vehiculos_comprados = None

    def comprar_vehiculo(self, vehiculo):
        if vehiculo.disponibilidad():
            print(f"{self.nombre} ha comprado un {vehiculo.marca} {vehiculo.modelo} del año {vehiculo.año}.")
            vehiculo.vender()
            self.vehiculos_comprados = vehiculo
        else:
            print(f"Lo siento, el {vehiculo.marca} {vehiculo.modelo} del año {vehiculo.año} no está disponible para la venta.")

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        if self.vehiculos_comprados:
            print(f"Vehículo comprado: {self.vehiculos_comprados.marca} {self.vehiculos_comprados.modelo} del año {self.vehiculos_comprados.año}")
        else:
            print("No ha comprado ningún vehículo aún.")
            
    def comprar_vehiculo(self, vehiculo):
        print(f"{self.nombre} ha comprado un {vehiculo.marca} {vehiculo.modelo} del año {vehiculo.año}.") #la f significa que se pueden usar variables dentro de las llaves {} para mostrar su valor en la cadena de texto. En este caso, se muestra el nombre del usuario y la información del vehículo que ha comprado.
        
    def ver_vehiculo_disponible(self, vehiculo):
        if vehiculo.disponibilidad() == False:
            print(f"{self.nombre} no puede comprar el {vehiculo.marca} {vehiculo.modelo} del año {vehiculo.año}.")


Vehiculo1= Vehiculo("Toyota", "Corolla", 2020)
#Vehiculo1.mostrar_informacion()
User1= User("Juan", 30)
User1.mostrar_informacion()
User1.ver_vehiculo_disponible(Vehiculo1)