may=0
man=100
num=1
cont=0
sm=0
pr=0
contnum=0
while num!=0:
    num=int(input('ingrese numero'))
    cont=cont+1 #cont+=1
    sm+=num
    pr=sm/cont
contnum=num
if  contnum<may:
    may=contnum
if contnum>man and contnum!=0:
    man=contnum
    


print(f'El usuario ingreso {cont-1} numeros')
print(f'la suma de todos los numeros ingresados  es {sm} ')
print(f'el promedio de la suma es {pr}')
print(f'el numero mayor es {may}' )
print(f'el numero menor es {man}')

#print('El usuario ingreso', cont, 'numeros')