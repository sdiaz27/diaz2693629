maximo = 0
num = 0

while num >= 0:
    num = int(input("Introduce un número positivo (introduce un número negativo para terminar): "))
    if num > maximo:
        maximo = num

print("El número máximo introducido es:", maximo)
