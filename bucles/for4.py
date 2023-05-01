# Función para calcular la suma de los divisores de un número
def sum_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

# Pedimos al usuario que ingrese los dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Calculamos la suma de los divisores de cada número
sum1 = sum_divisors(num1)
sum2 = sum_divisors(num2)

# Verificamos si los números son amigos
if sum1 == num2 and sum2 == num1:
    print("Los números", num1, "y", num2, "son números amigos.")
else:
    print("Los números", num1, "y", num2, "no son números amigos.")
