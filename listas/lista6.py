# Pedimos la cantidad de dígitos al usuario
n = int(input("Introduzca la cantidad de dígitos que desea en la serie de Fibonacci: "))

# Inicializamos el arreglo con los dos primeros valores de la serie
fibonacci = [1, 1]

# Añadimos valores al arreglo mientras la longitud de la serie sea menor que n
while len(fibonacci) < n:
    # Calculamos el siguiente valor sumando los dos últimos valores
    next_value = fibonacci[-1] + fibonacci[-2]
    # Añadimos el valor al arreglo
    fibonacci.append(next_value)

# Imprimimos el arreglo con la serie de Fibonacci
print("Serie de Fibonacci con", n, "dígitos:", fibonacci)