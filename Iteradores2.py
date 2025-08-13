#Ejemplo de iterador

#Crear una lista 
my_list = [1, 2, 3, 4, 5]
# Crear un iterador de la lista

#Obtener el iterador
my_iter = iter(my_list) # Funcion iter() devuelve un iterador de la lista

#Usar el iterador
print(next(my_iter))  # Imprime el primer elemento (1) next ayuda a ver que valor se almacena en memoria
print(next(my_iter))  # Imprime el segundo elemento (2)
print(next(my_iter))  # Imprime el tercer elemento (3)      
print(next(my_iter))  # Imprime el cuarto elemento (4)
print(next(my_iter))  # Imprime el quinto elemento (5)
# print(next(my_iter))  # Esto generará un error StopIteration porque no hay más elementos



#Iterar en cadenas
# Crear una cadena
TEXTO = "Hola, mundo"
# Crear un iterador de la cadena el iterador de la cadena
# es un objeto que permite recorrer la cadena carácter por carácter
iterador_texto = iter(TEXTO)

# Usar el iterador

for caracter in iterador_texto:  # Por cada carácter en el iterador de la cadena
    print(caracter)  # Imprime cada carácter de la cadena


#---------------------------------------------------------------------------------------------------
# Iterador para los números impares
# Límite    
limite = 10
# Crear un iterador para los números impares
iterador_impares = iter(range(1, limite + 1, 2)) # Itera cada dos numeros 

# Usar el iterador
for impar in iterador_impares:  # Por cada número impar en el iterador
    print(impar)  # Imprime el número impar 


#---------------------------------------------------------------------------------------------------
# Iterador para los números pares
# Límite    
limite = 10
# Crear un iterador para los números pares
iterador_pares = iter(range(0, limite + 1, 2)) # Itera cada dos numeros

# Usar el iterador
for par in iterador_pares:  # Por cada número par en el iterador
    print(par)  # Imprime el número parç


#---------------------------------------------------------------------------------------------------
def my_generator():  # Un generador simple
    """Un generador simple que produce los números 1, 2 y 3. cierto que no retorna, genera con yield"""
    yield 1  # Genera el número 1 
    yield 2  # Genera el número 2
    yield 3  # Genera el número 3

# Usar el generador
for valor in my_generator():  # Por cada valor generado por el generador
    print(valor)  # Imprime el valor generado


#---------------------------------------------------------------------------------------------------
# Generador de la secuencia de Fibonacci
def fibonacci(limit):   # Función generadora de la secuencia de Fibonacci
    """Generador de la secuencia de Fibonacci hasta un límite especificado."""
    a, b = 0, 1
    while a < limit:
        yield a  # Genera el número actual de la secuencia
        a, b = b, a + b  # Actualiza los valores para la siguiente iteración

for num in fibonacci(10):  # Por cada número en la secuencia de Fibonacci hasta el límite especificado
    print(num)  # Imprime el número de la secuencia de Fibonacci