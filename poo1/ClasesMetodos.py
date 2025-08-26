class Person:
    def __init__(self, name, age): #_init_ es el constructor, el cual se llama a el mismo y llama otros parametros deseados
        self.name = name #esto es como el this.name en java
        self.age = age
#esto era el constructor

    def greet(self): #Esta es la nomenclatura cuando estamos usando funciones propias de nuestra clase.
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años.") #f es un modificador que permite incluir variables dentro de cadenas de texto. darle un formato mas legible.

person1 = Person("Juan", 30)
person2 = Person("Maria", 25)
person1.greet()
person2.greet() 