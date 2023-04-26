# creamos dos variables con el mismo valor 
num1,num2=100,25
"""imprimimos 4 mensajes diferentes asiendole 
conocer al usuario las 4 opcciones que pude tomar """
print('1-sumar')
print('2-restar')
print('3-multiplicar')
print('4-dividir')
#creamos una variable llamada selector donde el usuario registrarra la opcion deseada
selector=(input('Digite la opcion'))
#utilizamos mach para saver cual es la opccion que ligio el usuario como una condiciopnal 
match selector:
    #case indiaca la operacion que eligio
    #  segun lo introducido por el usario segu8an esto ara lo que se pida bien sea  +,-,*,/
    case '1':
        print(num1+num2)
    case '2':
        print(num1-num2)
    case '3':
        print(num1*num2)
    case '4':
        print(num1/num2)
    