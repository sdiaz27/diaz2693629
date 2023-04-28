# Solicitar los valores inicio, fin y cantidad
inicio = int(input("Ingrese el valor de inicio: "))
fin = int(input("Ingrese el valor de fin: "))
cantidad = int(input("Ingrese la cantidad a incrementar o decrementar: "))

# Verificar si la cantidad es positiva o negativa
if cantidad > 0:
    # Ciclo for para incrementar
    for i in range(inicio, fin+1, cantidad):
        print(i)
else:
    # Ciclo for para decrementar
    for i in range(inicio, fin-1, cantidad):
        print(i)
