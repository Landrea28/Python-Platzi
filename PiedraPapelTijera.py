userOne = input("Jugador 1, ingrese su jugada (piedra, papel o tijera): ").lower()
userTwo = input("Jugador 2, ingrese su jugada (piedra, papel o tijera): ").lower()

if userOne == userTwo:
    print("Empate, ambos jugadores eligieron:", userOne)
elif (userOne == "piedra" and userTwo == "tijera") or \
     (userOne == "papel" and userTwo == "piedra") or \
     (userOne == "tijera" and userTwo == "papel"):
    print("Jugador 1 gana:", userOne, "vs", userTwo)        
else:
    print("Jugador 2 gana:", userTwo, "vs", userOne)    
print("Fin del juego")
# Ejemplo de uso de operadores lógicos

list(range(10))  # Crea una lista de números del 0 al 9
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Ejemplo de uso de range
list(range(1, 11))  # Crea una lista de números del 1 al 10
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Ejemplo de uso de range con paso
list(range(1, 11, 2))  # Crea una lista de números del 1 al 10 con paso 2
[1, 3, 5, 7, 9]

