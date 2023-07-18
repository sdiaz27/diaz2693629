
from persona import *

ob1=persona('juan', 1031587)
print(type (ob1))
print(ob1.getnombre())
print(ob1.getdocumento())
ob1.setcursos('HTML')
print(ob1.getcursos())
ob1.setcursos('CSS')
print(ob1.getcursos())


ob1.deletecursos('CSS')
print(ob1.getcursos())

ob1.deletecursos('hola')