#listas
to_do = ["Dirigirnos al hotel",
"Ir a almorzar",
"Visitar museo",
"Volver al hotel"]
print(to_do)
numeros = [1,2,3,4, "cinco"]
print(type(numeros))
print(numeros)
mix = ["uno", 2, 3.14, True, [1, 2, 3]]
print(mix)
print(len(mix))
print("primer elemento", mix[0])
print("segundo elemento", mix[1])
print("ultimo elemento", mix[-1])
texto = "Hola mundo"
print("primer elemento", texto[0])
print("segundo elemento", texto[1])
print("ultimo elemento", texto[-1])
print(mix[2:-2]) #desde x hastala posicion y
print(mix)
mix.append(False) #añadir al final x elemento
print(mix)
mix.append(["a", "b"])
print(mix)
mix.insert(1, ["a","b"]) #añade a la posicion numero 1
print(mix)
print(mix.index(["a","b"]))#consultar la posicion
num = [1, 2, 100, 90.54, 3, 4, 5]
print(num)
print("Mayor: ",max(num))
print("Menor: ",min(num))
del num[-1] #elimina el dato marcado en la posicion
print(num)
del num [:2]
print(num)
del num #elimina toda la lista
print(num)