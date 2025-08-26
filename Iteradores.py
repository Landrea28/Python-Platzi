# ITERACIONES

# Ejemplo de uso de for
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)  # Imprime cada número en la lista
for i in range(1, 6):
    print(i)  # Imprime números del 1 al 5  
for i in numbers:
    print("i is equal to: ", i + 1)  # Imprime cada número en la lista
for i in range(10):
    if i % 2 == 0:
        print(i, "es par")  # Imprime números pares del 0 al 9
    else:
        print(i, "es impar")  # Imprime números impares del 0 al 9
for i in range(10):
    if i == 5:
        print("Se encontró el número 5, saliendo del bucle")
        break  # Sale del bucle cuando i es igual a 5
    print(i)  # Imprime números del 0 al 4
for i in range(10):
    print(i)  # Imprime números del 0 al 9

fruits = ["manzana", "banana", "naranja"]
for fruit in fruits:
    if fruit == "banana":
        print("Se encontró una banana, continuando con el siguiente elemento")
        continue  # Salta a la siguiente iteración cuando se encuentra una banana
    print(fruit)  # Imprime cada fruta excepto la banana
x = 0
while x < 5:
    if x == 3:
        print("x es igual a 3, saliendo del bucle")
        break
    print("x es igual a:", x)  # Imprime el valor de x
    x += 1  # Incrementa x en 1


number = [1, 2, 3, 4, 5]
for i in number:
    print("Aqui i es igual a : ",i+1)  # Imprime cada número en la lista incrementado en 1
for i in range(3, 10):
    print(i) # Imprime números del 3 al 9

fruit = ["manzana", "banana", "cereza"]
for f in fruit:
    if f == "banana":
        print(f)
        print("Se encontró una banana, continuando con el siguiente elemento")
        continue  # Salta a la siguiente iteración cuando se encuentra una banana
    print(f)  # Imprime cada fruta excepto la banana
x = 0
while x < 5:
    if x == 3:
        print("x es igual a 3, saliendo del bucle")
        break  # Sale del bucle cuando x es igual a 3
    print("x es igual a:", x)  # Imprime el valor de x
    x += 1  # Incrementa x en 1
# break detiene, continue omite


# CLASE 2 ITERACIONES

#crea una lista de numeros del 1 al 5
my_list = [1, 2, 3, 4, 5]
# Itera sobre la lista y muestra cada elemento
myIter = iter(my_list)

#Usar el iterador 
print(next(myIter))  # Imprime el primer elemento (1)
print(next(myIter))  # Imprime el segundo elemento (2)
print(next(myIter))  # Imprime el tercer elemento (3)
print(next(myIter))  # Imprime el cuarto elemento (4)   
print(next(myIter))  # Imprime el quinto elemento (5)
# print(next(myIter))  # Esto generará un error StopIteration porque no hay más elementos   

#Iterar en cadenas 
#crear cadena
texto_0 = "Hola, mundo"
# Crear un iterador de la cadena
texto_iter = iter(texto_0)  

#Iterar sobre la cadena
for char in texto_iter: #por cada carácter en el iterador de la cadena
    print(char)  # Imprime cada carácter de la cadena


#Iterardor para los numeros impares
#Limite 
limite = 10
# Crear un iterador para los números impares
oddIter = iter(range(1, limite+1,2))

#Usar el iterador
for odd in oddIter:  # Por cada número impar en el iterador
    print(odd)  # Imprime cada número impar hasta el límite especificado





def myGenerator(): #un generador simple
    """Un generador simple que produce los números 1, 2 y 3."""
    yield 1  # Genera el número 1
    yield 2  # Genera el número 2
    yield 3  # Genera el número 3 generador no retorna, genera

# Usar el generador
for value in myGenerator():  # Por cada valor generado por el generador
    print(value)  # Imprime cada valor generado (1, 2, 3)


def fibonacci(limit):  # Generador de la secuencia de Fibonacci
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for num in fibonacci(10):  # Por cada número en la secuencia de Fibonacci hasta el límite especificado
    print(num)  # Imprime cada número de la secuencia de Fibonacci (0, 1, 1, 2, 3, 5, 8)    
