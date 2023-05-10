#importamos la carpeta de funciones random
import random

num=(input('escriba el numero a saber: '))
tam=10
#definimos la funcion (espesificamos tamañano y rango ) 
def llenarLista(tam,rango):
#creamos lista por comprencion 
    lista=[random.randrange(rango) for i in range(tam)]
#retornamos la lista para llenar la l1 y dar el tamño y rango  a la funcion
    
    return lista
#definimos la funcion

def sumaLista(lista):
    sum=0
#hacemos la operacion aricmetica 
    for x in lista:
        sum+=x
    return sum
#definimos la funcion
def promedioLista(lista):
#hacemos la operacion aricmetica po comprencion 
    return sumaLista(lista)/len(lista)

def mayor(lista):
    max=lista[0]
    for x in lista:
        if x > max:
            max=x
    return max

def menor(lista):
    men=lista[0]
    for x in lista:
        if x < men:
            men=x
    return men

def ordenasendente (lista,tam):
    for i in range(len(lista)):
     for j in range(i+1,tam):
        if lista[i]>lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
    return lista

def desendente (lista,tam):
    for i in range(len(lista)):
     for j in range(i+1,tam):
        if lista[i]<lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
    return lista

def moda (lista):
    Moda = None
    Cantidad = 0
    for index, numero in enumerate (lista) :
        cantidadVecesAparece = lista.count (numero)
        if cantidadVecesAparece > Cantidad :
            Cantidad = cantidadVecesAparece
            Moda = numero
    return Moda        

def mediana (lista):
    data = sorted(lista)
    index = len(data) // 2    
    if len(lista) % 2 != 0:
        return data[index]
    return (data[index - 1] + data[index]) / 2


def saber (lista, num):
    encontrado = False
    posiciones = []
    contador = 0

    for i in range(len(lista)):
        if lista[i] == num:
            encontrado = True
            posiciones.append(i)
            contador += 1

    if encontrado:
        print("El número", num, "fue encontrado.")
        print("Se encontró en la(s) posición(es):", posiciones)
        print("Se repite", contador, "veces.")
    else:
        print("El número", num, "no fue encontrado.")
    return encontrado
        

    
    
#imprimimos en la consola
l1=llenarLista(tam,10)
print(f'la lista es: {l1}')
print(f'la suma de la lista es: {sumaLista(l1)}')
print(f'el promedio de la lista es: {round(promedioLista(l1),2)}')
print(f'el numero mayor de la lista es: {mayor(l1)}')
print(f'el numero menor de la lista es: {menor(l1)}')
print(f'el orden de la lista acendente es: {ordenasendente(l1,tam)}')
print(f'el orden de la lista decendente es: {desendente(l1,tam)}')
print(f'la moda de la lista es: {moda(l1)}')
print(f'la mediana de la lista es: {mediana(l1)}')
print(f'{saber(l1,num)}')

