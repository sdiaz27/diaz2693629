import random


lista = []
tem = int(random.randint(10, 20))
for i in range(tem):
    num =(random.random(100))
    lista.append(num)
print(lista)
for i in range(len(lista)):
    for j in range(i+1,tem):
        if lista[i]>lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
print(lista)
            