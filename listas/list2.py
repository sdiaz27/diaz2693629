import random
lista=[]
tem=int(random.randint(10,20))
sum=0
pro=0
may=0
men=999
for i in range(tem):
    num=int(random.randrange(100))
    lista.append(num)
    sum+=num
    pro=sum/tem
    if num > may:
        may=num
    if num < men:
        men=num
print(lista)
print (f'lasumadelosnumeros es : {sum} ' )
print (f'le promedio de los  mumero es :  {pro}')
print (f'el numero mayor es :  {may}')
print (f'el numero menor es :  {men}')


