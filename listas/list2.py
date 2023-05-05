import random

lista = []
tem = int(random.randint(10, 20))
sum = 0
pro = 0
may = 0
men = 999
mida = 0

# Calcula la lista de números y realiza otros cálculos
for i in range(tem):
    num =(random.random(100))
    lista.append(num)
    sum += num
    pro = sum / tem
    if num > may:
        may = num
    if num < men:
        men = num

# Calcula la moda
frecuencias = {}
for num in lista:
    if num in frecuencias:
        frecuencias[num] += 1
    else:
        frecuencias[num] = 1

max_frecuencia = max(frecuencias.values())
moda = min([k for k, v in frecuencias.items() if v == max_frecuencia])

# Calcula la mediana
lista.sort()
n = len(lista)
if n % 2 == 0:
    mediana = (lista[n // 2 - 1] + lista[n // 2]) / 2
else:
    mediana = lista[n // 2]

print(lista)
print(f'La suma de los números es: {sum}')
print(f'El promedio de los números es: {pro}')
print(f'El número mayor es: {may}')
print(f'El número menor es: {men}')
print(f'La mediana es: {mediana}')
print(f'La moda es: {moda}')


