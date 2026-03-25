""" Lista de números → mostrar el mayor
Pedir un número por teclado y decir si es par o impar
Usar .append() correctamente (aquí lo entiendes de verdad)"""

# Lista de números → mostrar el mayor
numeros= [1,4,8,30,24,5,7,400,7,9,6888,370,60,35,56,680,37,0,60,4,8,0,4,0]
mayor = max(numeros) # Para mostrar el mayor de la lista, se puede usar la función max()
print("El número mayor de la lista es:", mayor)

# Pedir un número por teclado y decir si es par o impar
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# Usar .append() correctamente (aquí lo entiendes de verdad)
lista = [] # Se crea una lista vacía    
for i in range(5): # Se pide al usuario que ingrese 5 números
    numero = int(input("Ingrese un número: "))
    lista.append(numero) # Se agrega el número a la lista usando .append()  
print("La lista de números ingresados es:", lista)
# El .append() se utiliza para agregar elementos a una lista existente. 
# En este caso, se agrega cada número ingresado por el usuario a la lista vacía creada al inicio.