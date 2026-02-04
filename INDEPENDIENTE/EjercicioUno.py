#Mostrar números pares del 1 al 20
#Recorrer una lista y mostrar solo los mayores a 10
#Crear una función simple (def) que sume dos números


# Mostrar números pares del 1 al 20
for i in range(1,21):
    if i % 2 == 0:
        print(i)
#,, Recorrer un,a, lista y mostrar solo los mayores a 10
numeros = [1,35,1,6,1,4,6,123,5,1,5,7,8,9,10,11,12]
print("Números mayores a 10:")
for numero in numeros:
    if numero > 10:
        print(numero)

# Crear una función simple (def) que sume dos números 
def numeros (a,b):
    sumar = a + b
    return sumar

resultado = numeros(5,7)
print("La suma es:", resultado)