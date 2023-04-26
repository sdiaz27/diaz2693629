#se crean dos variable (y,x) con valosres (5,3)
x=5
y=3
#ponemos while y negamos  la condicion para determinar si sion factores o no si los son terminara el programa y sino ara un bucle 
while not (x%y==0 or y%x==0): 
#imprimimos en pantalla        
    print('Rutina para saber si dos numeros son factores')
#ponemos dos variable (y,x) y les damos input para que el usuario ingerse el valor    
    x=int(input('ingrese numero'))
    y=int(input('ingrese numero'))   
    #imprimimos (don factores )para indicar al usuario que a terminado el programa 
print('Son factor')