n = int(input("Introduce el número de líneas que quieres imprimir: "))

i = 1
while i <= n:
    linea = ""
    j = 1
    while j <= i:
        linea += "* "
        j += 1
    print(linea)
    i += 1
