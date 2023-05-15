import random
list=[round(random.uniform(1.50,2.00),2) for i in range(15,125)]
tam=15,125
def ordenasendente (lista,tam):
    for i in range(len(lista)):
     for j in range(i+1,tam):
        if lista[i]>lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
    return lista

print(list)
print(len(list))
print(f'{ordenasendente (list,tam)}')