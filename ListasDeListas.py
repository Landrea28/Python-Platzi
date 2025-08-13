a = [1, 2, 3 ,4 ,5]
b = a
print(a)
print(b)
del a[0]
print(id(a)) #donde se almacena esta informacion
print(id(b))
#para que no todas las acciones que haga en una variable, se vean reflejadas en otra, usamos el metodo slice
c = a[:] #desde la posicion 0 hasta la final
print("")
print(id(a)) 
print(id(b))
print(id(c)) #ya accsedemos a lugares diferentes en memoria
a.append(6)
print(a)
print(b)
print(c)


#Listas de listas
# O matrices
#separar ideas en filas
#[[1 2 3],[4 5 6], [7 8 9]] separar en comas y cada uno representa una fila y una poisicion y lo mismo para columnas
matrix = [[1, 2 ,3], 
          [4, 5, 6],
          [7, 8, 9]]
print(matrix)
print(matrix[0])
#añadir una posicion mas e iterar a travez de estos elementos
matriz = [[[1,2], [3, 4]],[[5, 6],[7, 8]]] # dupla, cada [interno] 
numeritos = (1, 2, 3, 4, 5) #parentesis opcionales
print(numeritos)
print(type(numeritos)) #palabra reservada tuple -> significa tupla
print(numeritos[0])
#numeritos[0] = "unos" # para reemplazar en x posicion
#print(numeritos) # error ya que la tupla es inmutable, es decir que no se puede modificar 
