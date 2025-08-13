x = 10
if x > 5:
    print("x is greater than 5")        
else:
    print("x is not greater than 5")
print("afuera del if")
y = int (input("Ingrese un numero: "))
if y > 10:
    print("y is greater than 10")
elif y == 10:
    print("y is equal to 10")
else:
    print("y is not greater than 10")
# Ejemplo de uso de if-else

a = 5
b = 10
if a>2 and b<15:
    print("a is greater than 2 and b is less than 15")

if a>2 or b<5:
    print("a is greater than 2 or b is less than 5")    

if not (a == b):
        print("a is not equal to b")    
# Ejemplo de uso de operadores de comparación

is_member = True
age = 20
if is_member:
    if age >= 18:
        print("You can enter the club")
    else:
        print("You cannot enter the club")  
else:
    print("You cannot enter the club because you are not a member and you are not an adult")
# Ejemplo de uso de operadores de comparación
# Ejemplo de uso de operadores lógicos