import random
tam=random.randrange(5,20)
lista=[random.randrange(100) for i in range(tam)]
rebanada= lista[len(lista)//2:-1]
print(lista)
print(rebanada)
