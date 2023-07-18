try :
    import math
except ImportError:
    print("Error: No se pudo importar el módulo math")
try:    
    a=(float(input('Esciba el valor de a: ')))
    b=(float(input('Esciba el valor de b: ')))
    c=(float(input('Esciba el valor de c: ')))
except ValueError:
    print('Error: El valor no es (float)')

def calcular_raices(a, b, c):
    discriminante = b**2 - 4*a*c
    try:
        if discriminante > 0:
            raiz_1 = (-b + math.sqrt(discriminante)) / (2*a)
            raiz_2 = (-b - math.sqrt(discriminante)) / (2*a)
            print("Las raíces son reales y diferentes:")
            print("Raíz 1 =", raiz_1)
            print("Raíz 2 =", raiz_2)
        elif discriminante == 0:
            raiz = -b / (2*a)
            print("La ecuación tiene una raíz real:")
            print("Raíz =", raiz)
        else:
            parte_real = -b / (2*a)
            parte_imaginaria = math.sqrt(-discriminante) / (2*a)
            print("Las raíces son complejas y conjugadas:")
            print("Raíz 1 =", parte_real, "+", parte_imaginaria, "i")
            print("Raíz 2 =", parte_real, "-", parte_imaginaria, "i")
    except ZeroDivisionError:
        print('Error: no se pue4de dividir por (0)')

try:
    calcular_raices(a,b,c)
except NameError:
    print('Error:el valor introducido no es un (numero)')