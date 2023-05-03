# Pedimos al usuario que introduzca los dos números
m = int(input("Introduce el primer número: "))
n = int(input("Introduce el segundo número: "))

# Aplicamos el algoritmo de Euclides
while n != 0:
    r = m % n
    m = n
    n = r

# Mostramos el resultado
print("El m.c.d de los dos números es:", m)
