import random

def calcular_percentiles():
    # Definir rango de estaturas
    estatura_minima = 1.50
    estatura_maxima = 2.00

    # Definir cantidad de estaturas
    cantidad_estaturas = random.randint(15, 125)

    # Crear lista de estaturas
    estaturas = []
    for _ in range(cantidad_estaturas):
        estatura = round(random.uniform(estatura_minima, estatura_maxima), 2)
        estaturas.append(estatura)

    # Ordenar la lista de estaturas
    estaturas.sort()

    # Calcular percentiles
    percentiles = [0, 25, 50, 75, 100]
    percentile_values = []
    for percentile in percentiles:
        index = int(percentile / 100 * (cantidad_estaturas - 1))
        percentile_value = estaturas[index]
        percentile_values.append(percentile_value)

    # Imprimir percentiles
    print("Percentiles:")
    for i, percentile in enumerate(percentiles):
        print(f"{percentile}%: {percentile_values[i]}")

# Llamar a la función
calcular_percentiles()