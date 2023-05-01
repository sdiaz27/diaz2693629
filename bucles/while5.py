numeros = input("Ingrese dos números separados por un espacio: ")
num1, num2 = map(int, numeros.split())
mayor = max(num1, num2)
menor = min(num1, num2)

resultado = mayor - menor

if resultado >= menor:
    resultado -= menor
    print("El resultado de restar el menor del mayor y restar nuevamente es:", resultado)
else:
    print("El resultado de restar el menor del mayor es:", resultado)

