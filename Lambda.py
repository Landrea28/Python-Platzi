add= lambda a, b: a + b 
print(add(10,4))

multiply = lambda a, b: a * b
print(multiply(80,5))

#Cuadrado de cada numero
numbers = range(11) # como son los numeron del 0 al 10 se puede dejar simplemente el 11
square = list(map(lambda x : x**2, numbers)) #map() Aplica una función a cada elemento de un iterable.
print("Cuadrados:",square)

#Pares
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Pares:", even) #filter() Filtra cada elemento de un iterable a traves de una función

"""
reduce()
Toma los dos primeros elementos de un iterable y aplica una función.
Toma el resultado anterior y el elemento siguiente y aplica la función.
Repite hasta acabar con todos los elementos del iterable.
"""
from functools import reduce  # Necesario importar reduce

#Suma
total = reduce(lambda x, y: x + y, numbers)
print("Suma total:", total)

"""
Estas funciones retornan un elemento iterador, por eso es necesario 
usar la función list() para convertirlo en un elemento iterable.
"""

#Lambda es una función anónima que solo necesita parámetros y una operación para aplicar a ella