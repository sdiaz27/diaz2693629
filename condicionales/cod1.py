#creamos  dos variable llamadas x, y y le desimos a el usuario que introdusca los valores de las variables  
x=input('ingrese numero')
y=input('ingrese numero')
#condisionamos con el si y desimos que si x es igual a y 
if x==y:
    #si esto esverdadero imprimira un mensage  "son iguales "
    print('son iguales')
    #si no entonses si x es > que y  imprimira "decendente"
elif x>y:
    print('descendente')
    #si no entoses  imprimira "asendente"
else:
    print('ascendente')