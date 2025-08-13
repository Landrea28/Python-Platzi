numbers = {1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco"}
print(numbers)
# Acceso a un valor por su clave
print(numbers[1])  # Imprime "uno"      
# Acceso a un valor por su clave
print(numbers[3])  # Imprime "tres"
informacion = {
    "nombre": "Lina",
    "edad": 18,
    "ciudad": "Bogota",
    "lenguajes": ["Python", "JavaScript", "Java"]
}
print(informacion)
# Acceso a un valor por su clave
del informacion["edad"]  # Elimina la clave "edad"
print(informacion)  # Imprime el diccionario sin la clave "edad"
# Acceso a un valor por su clave
print(informacion["nombre"])  # Imprime "Lina"  
claves = informacion.keys()  # Obtiene las claves del diccionario
print(claves)  # Imprime las claves del diccionario 
print(type(claves))  # Imprime el tipo de las claves (dict_keys)
valores = informacion.values()  # Obtiene los valores del diccionario
print(valores)  # Imprime los valores del diccionario
print(type(valores))  # Imprime el tipo de los valores (dict_values) 
pairs = informacion.items()  # Obtiene los pares clave-valor del diccionario
print(pairs)  # Imprime los pares clave-valor del diccionario   
contacts = {
    "Lina Bello": {
        "nombre": "Lina",
        "edad": 18,
        "ciudad": "Bogota",
        "lenguajes": ["Python", "JavaScript", "Java"]
    },
    "Carlos Martinez": {
        "nombre": "Carlos",
        "edad": 22,
        "ciudad": "Medellín",
        "lenguajes": ["Python", "C++"]
    }
}
print(contacts)  # Imprime el diccionario de contactos
# Acceso a un contacto por su nombre
print(contacts["Lina Bello"])  # Imprime la información de Lina
print(contacts["Carlos Martinez"])  # Imprime la información de Carlos