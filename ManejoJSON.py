import json

#Lectura de un archivo JSON
with open('PythonPracticas.json', mode='r') as file:
    data = json.load(file)
    print(data)

#Mostrar el contenido
for item in data:
    print(f"Producto: {item['dispositivo']}, Marca: {item['marca']}")


#Añadir informacion a un archivo JSON
new_data = {
    'id': '7', 
     'dispositivo': 'Tablet', 
     'marca': 'Lenovo', 
     'categoria': 'Electronica'}

with open('PythonPracticas.json', mode='r') as file:
    products = json.load(file) #cargar el contenido existente del archivo JSON
    
products.append(new_data) #agregar el nuevo producto a la lista de productos

with open('PythonPracticas.json', mode='w') as file:
    json.dump(products, file, indent=4) #escribir la lista actualizada de productos en el archivo JSON con una indentación de 4 espacios para mejorar la legibilidad

