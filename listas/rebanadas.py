'''llene una lisat con numeros aleatorios (reales con decimales ) que representen calificasiones de un curso. 
Se evalua de 0 a 5 .
El curso puede tener etre 20 y 30 aprendices .
halla
1genere listas nuevas para los aprobados y los reprobados (se apreuba con 3 )
2 genere listas nuevas para cada unidad, es decir ,los que sacan de 0 a  1 son 
in grupo, los de 1 a 2  otro grupo y asi secesivamente 
3 diga cual es el promedio de los que aprovaron y de los que reprovaron por 
sepaerado.'''


import random


tam=random.randrange(20,30)
lista=[round(random.uniform(0.,5.), 1) for i in range(tam)]

print(lista)

for i in range(len(lista)):
    for j in range(i+1,tam):
        if lista[i]>lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
print(lista)

ind=0 
for x in lista:
    if x >= 3.0:
        ind=x
print(ind)

#Apro=lista[ind:]
#Rpro=[]
    
        
#print(Apro)
#print(Rpro)
        