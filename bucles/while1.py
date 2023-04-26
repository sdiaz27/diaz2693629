#damos nopmbre a una variable 
i=1
#damos nombre a la segunda variable 
sum=0.
#ponemos hwail y decimos que si la bariable i es menor o igual a 10   va arealisar la sieguente funcion 
while i<=10:
    #imprimimos en la consola l avariable i 
    print(i)
    # desimos que la nos guarde el resultado en la bariable sum y que  a esta misma se le adicione  el valor de la variable i 
    sum+=i #sum=sum+i
    # desimos que la nos guarde el resultado en la bariable i y que  a esta misma se le adicione  1
    i+=1 #i=i+1
    #imprimimos la variable sum 
print('la suma es:',sum)
# creamos una variable llamada sp, si y otrorgamois un valor 

i=0
sp,si=0,0
#ponemos hwail y decimos que si la bariable i es menor o igual a 10   va arealisar la sieguente funcion 
while i<=10:
    #imprimimos en la consola l avariable i 
    print(i)
    #ponemos cuna condicion si y damos las valores por los cuales vamos a operar i 
    if i%2==0:
        #agregamos la variable sp donde almacenara el resultado y a la misma le sumamos  la variable i 
        sp+=i
        #si no es asi  entonses la variable si se guardara el resultado de la operacion  si mas i 
    else:
        si+=i
        #y en la variable i se va a guardar la operacion i mas 1 
    i+=1
    # se imprime en pantalla la variable sp
print('la suma de los pares es:',sp)
#o sino se imprime en pantalla la variable sp
print('la suma de los impares es:',si)