import csv

#Leer un archivo CSV y devolver una lista de diccionarios
with open('PythonPracticas.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)

#Mostrar la informacion por colomnas
with open('PythonPracticas.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"id: {row['id']}, dispositivo: {row['dispositivo']}, marca: {row['marca']}, categoria: {row['categoria']}") 

import csv

new_data = {
    'id': '6', 
     'dispositivo': 'Tablet', 
     'marca': 'Apple', 
     'categoria': 'Electronica'}

with open('PythonPracticas.csv', mode='a', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=new_data.keys())
    csv_writer.writeheader() #escribir el encabezado del archivo CSV
    csv_writer.writerow(new_data) #escribir una fila de datos en el archivo CSV


#new column

import csv

file_path = 'PythonPracticas.csv'
updated_file_path = 'PythonPracticas_updated.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    #Obtener nombres de las columnas existentes y agregar el nuevo campo 'precio'
    fieldnames = csv_reader.fieldnames + ['Precio'] #agregar el nuevo campo 'precio' a la lista de campos existentes
    
    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader() #escribir el encabezado del nuevo archivo CSV
        for row in csv_reader:
            row['Precio'] = '100' #asignar un valor de precio a cada fila
            csv_writer.writerow(row) #escribir la fila actualizada en el nuevo archivo CSV