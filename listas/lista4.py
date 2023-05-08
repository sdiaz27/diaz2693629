
import random


lista=[random.randint(0,9) for i in range(random.randint(15,20))]
print('se generaron :',(len(lista)), 'numeros')
print(f'los numeros son :  {lista}')

num=int(input('ingrese el numero que quiera buscar : '))

rep=0
for i in lista:                                                                                                                                
    if i ==num:
     rep+=1
    
if rep > 0:
     print('el numero si esta' )
else:
    print('el numero no esta ')        
    
print(f'El numero esta {rep}')

for x in range(len(lista)):
    print (lista.index(num))
    