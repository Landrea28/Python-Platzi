#clase numero 1
#escribir phynon, instalador pagina oficial con el sistema operativo, terminal (python) acceso al interprete de python
print("Hola mundo") 
#syntax error ->
#tener cuidado con la sangria
#variables
saludo = "Hola"
print(saludo)

nombre_1 = "Lina"
print(saludo, nombre_1)

print(type(nombre_1))
name = '''ANDREA
Bello''' #salto de linea
#indexacion (puesto de los caracteres de una cadena de texto, por ejemplo)
print(nombre_1[0])
print(nombre_1[1])
print(nombre_1[2])
print(nombre_1[3])
print(nombre_1[-1])

#El + no incluye espacios, la , si
print(saludo +" "+ nombre_1)
print(saludo + nombre_1)

#como el .length en java, cantidad de caracteres
print(nombre_1*5)
print(len(name))
print(len(nombre_1))


print(name.lower())#todo en minuscula
print(name.upper())#todo en mayuscula
print(name.strip())#elimina espacios
#comentario