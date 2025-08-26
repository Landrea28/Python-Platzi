
try:
    divisor = int(input("Ingrese un divisor: "))
    resultado = 10 / divisor
    print("El resultado es:", resultado)
except ValueError as e:
    print("Por favor, ingrese un número válido.")
    print("Error:", e)
except ZeroDivisionError as e:
    print("Error: No se puede dividir entre cero.")
    print("Error:", e)


#Esta linea de codigo nos permite poder ver los tipos de excepciones como clases y sus subclases
"""

def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

print_exception_hierarchy(Exception)

"""