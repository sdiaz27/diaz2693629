# Solicitar el número y el valor de n
numero = int(input("Ingrese un número positivo: "))
n = int(input("Ingrese el valor de n: "))

# Verificar que el número ingresado sea positivo
if numero <= 0:
    print("El número ingresado no es positivo.")
else:
    # Contador de múltiplos de n
    contador = 0
    
    # Ciclo for para recorrer la serie
    for i in range(numero+1):
        if i % n == 0:
            contador += 1
    
    # Imprimir el resultado
    print("Hay", contador, "múltiplos de", n, "en la serie desde cero hasta", numero)
