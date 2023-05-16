import random
tam=10
def Lista1(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]
    return lista
def Lista2(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

l1=Lista1(10,100)
l2=Lista2(10,100)

def sumaLista(lista1,lista2):
    sum1=0
    for x in lista1:
        sum1+=x
    
    sum2=0
    for x in lista2:
        sum2+=x    
    
    smayor=0
    if sum1>sum2:
        smayor = sum1
    else:
        smayor = sum2
    return sum1,sum2,smayor


def numeromayor (lista1,lista2):
    max=lista1[0]
    for x in lista1:
        if x > max:
            max=x
            
    max1=lista2[0]
    for x in lista2:
        if x > max1:
            max1=x
            
    mayor=0
    if max>max1:
        mayor = max
    else:
        mayor = max1
    return mayor


def numeromenor (lista1,lista2):
    men=lista1[0]
    for x in lista1:
        if x < men:
            men = x
            
    men1=lista2[0]
    for x in lista2:
        if x < men1:
            men1=x
            
    menor=0
    if men<men1:
        menor = men
    else:
        menor = men1
    return menor


def promedio (lista1,lista2):
    pro=0
    pro=lista1+lista2
    sum=0
    for x in pro:
        sum+=x
    
    return sum/len(pro)
    
def primos(lista1,lista2):
    pri=0
    pri=lista1+lista2
    for i in range(2,pri):
        if (pri%i) == 0:
            i=pri
            
    return pri



print(f'la lista es: {l1}')
print(f'la lista es: {l2}')
print(f'la suma mayor es : {sumaLista(l1, l2)}')
print(f'el numero mayor entre las listas es : {numeromayor(l1,l2)}')
encontrado = False
for i in range(len(l1)):
    if l1[i] == numeromayor:
        encontrado = True
        print('la lista con el numero mas grande es la : l1') 
    else:
        print('la lista con el numero mas grande es la : l2')
print(f'el numero menor entre las lista es : {numeromenor(l1,l2)}')
encontrado = False
for i in range(len(l1)):
    if l1[i] == numeromenor:
        encontrado = True
        print('la lista con el numero mas pequeño es la : l1') 
    else:
        print('la lista con el numero mas pequeño es la : l2')
print(f'el promedio de las lista es : {promedio(l1,l2)}')
print(f'los numeros primos son :  {primos(l1,l2)}')