def es_perfecto(num):
    suma=0
    for i in range(1,num):
        if num%i==0:
            suma+=i
    return suma==num
num=int(input("digite un numero: "))
if es_perfecto(num):
    print(num, "es un número perfecto")
else:
    print(num, "no es un número perfecto")
