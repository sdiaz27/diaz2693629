import random

# Pedimos el valor de n al usuario
n = int(input("Introduzca el valor de n: "))

# Inicializamos los arreglos con valores aleatorios generados por la función random
array1 = [random.randint(1, 100) for _ in range(n)]
array2 = [random.randint(1, 100) for _ in range(n)]

# Calculamos la suma de los elementos de cada arreglo
sum1 = sum(array1)
sum2 = sum(array2)

# Imprimimos el arreglo con la suma más alta
if sum1 > sum2:
    print("El primer arreglo tiene la suma más alta.")
elif sum1 < sum2:
    print("El segundo arreglo tiene la suma más alta.")
else:
    print("Ambos arreglos tienen la misma suma.")

# Imprimimos el arreglo con el número más alto
max1 = max(array1)
max2 = max(array2)
if max1 > max2:
    print("El primer arreglo tiene el número más alto.")
elif max1 < max2:
    print("El segundo arreglo tiene el número más alto.")
else:
    print("Ambos arreglos tienen el mismo número más alto.")

# Imprimimos el arreglo con el número más bajo
min1 = min(array1)
min2 = min(array2)
if min1 < min2:
    print("El primer arreglo tiene el número más bajo.")
elif min1 > min2:
    print("El segundo arreglo tiene el número más bajo.")
else:
    print("Ambos arreglos tienen el mismo número más bajo.")

# Calculamos el promedio conjunto de los dos arreglos
avg = (sum1 + sum2) / (2 * n)
print("El promedio conjunto es:", avg)

# Calculamos el promedio de cada arreglo y comparamos
avg1 = sum1 / n
avg2 = sum2 / n
if avg1 > avg:
    print("El promedio del primer arreglo está por encima del promedio conjunto.")
elif avg1 < avg:
    print("El promedio del primer arreglo está por debajo del promedio conjunto.")
else:
    print("El promedio del primer arreglo es igual al promedio conjunto.")

if avg2 > avg:
    print("El promedio del segundo arreglo está por encima del promedio conjunto.")
elif avg2 < avg:
    print("El promedio del segundo arreglo está por debajo del promedio conjunto.")
else:
    print("El promedio del segundo arreglo es igual al promedio conjunto.")

# Contamos la cantidad de pares e impares de cada arreglo
even1 = sum(1 for x in array1 if x % 2 == 0)
odd1 = n - even1
even2 = sum(1 for x in array2 if x % 2 == 0)
odd2 = n - even2

# Imprimimos el arreglo con más pares
if even1 > even2:
    print("El primer arreglo tiene más números pares.")
elif even1 < even2:
    print("El segundo arreglo tiene más números pares.")
else:
    print("Ambos arreglos tienen la misma cantidad de números pares.")

# Imprimimos el arreglo con más impares
if odd1 > odd2:
    print("El primer arreglo tiene más números impares.")
elif odd1 < odd2:
    print("El segundo arreglo tiene más números impares.")
else:
    print("Ambos arreglos tienen la")

   