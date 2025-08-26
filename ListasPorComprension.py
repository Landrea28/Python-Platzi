squares = [x**2 for x in range(1, 11)] #** son los cuadrados elevados a...
print("Los cuadrados son:", squares) 

celsius = [0, 10, 20.1, 34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius] #formula
print("Las temperaturas en Fahrenheit son:", fahrenheit)


#ejercicios: numeros pares
evens = [x for x in range(1, 21) if x % 2 == 0] #si el numero es divisible entre 2
print("Los números pares son:", evens)


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("La matriz transpuesta es:", transposed)