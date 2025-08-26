def greet(name, last_name= "sin apellido"): #Esto sugiere que si no tiene apellido este mensaje es el que se va a mandar
    print("Hola,", name, last_name)

greet("Juan", "Perez")
greet("Ana") #Si no tiene apellido, se manda el mensaje por defecto
greet(last_name="Bello", name="Luis") #Se pueden mandar los parametros en cualquier orden
greet("Maria", "Gomez")



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b   
 
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: División por cero no permitida"
    return a / b

def calculator():
    while True:
        print("Seleccione la operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        opcion = input("Ingrese el número de la operación deseada: ")
        if opcion == "5":
            print("Saliendo de la calculadora...")
            break
        if opcion in ["1", "2", "3", "4"]:
            number1 = float(input("Ingrese el primer número: "))
            number2 = float(input("Ingrese el segundo número: "))
            if opcion == "1":
                print("Resultado:", add(number1, number2))
            elif opcion == "2":
                print("Resultado:", subtract(number1, number2))
            elif opcion == "3":
                print("Resultado:", multiply(number1, number2))
            elif opcion == "4":
                print("Resultado:", divide(number1, number2))
        else:
            print("Opción no válida. Intente de nuevo.")
calculator()