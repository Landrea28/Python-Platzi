def impares():
    for i in range(1, 11):
        if i % 2 != 0:
            yield i

def pares():
    for i in range(1, 11):
        if i % 2 == 0:
            yield i
# Ejemplo de uso de los generadores de números pares e impares
print("Números impares:")
for num in impares():
    print(num)
print("Números pares:")
for num in pares():
    print(num)  


#---------------------------------------------------------------------------------------------------

iterador_impares = iter(impares())  # Crear un iterador para los números impares
iterador_pares = iter(pares())  # Crear un iterador para los números pares

print("Iterador de números impares:")
for num in iterador_impares:  # Usar el iterador de números impares
    print(num)
print("Iterador de números pares:")
for num in iterador_pares:  # Usar el iterador de números pares
    print(num)  


""" Iteradores: Necesitan definir explícitamente los métodos __iter__() y __next__().
Generadores: Se definen usando una función con yield.  
Generadores: Son más simples de crear y usar, ya que no requieren definir métodos especiales.
Iteradores: Pueden ser más complejos y requieren más código para implementarlos."""