#importamos las clases aprendiz y curso
from Aprendiz import *
from Curso import *
#creamos el objeto indicandole sus propidades 
objeto=Aprendiz("Ana Kurnikova",123456,'ADSO',2693629)
#print(objeto.__dict__)
#creamos otro objeto para insertar en la lista los cursos 
objcurso=Curso("Programacion Software","tecnico")
#yamamos la funcion getter que emos crado para los cursos 
objeto.agregarCurso(objcurso)
#print(objeto.__dict__)
#yyamamos a componercursos para insertas mas cursos a la lista 
objeto.componerCurso()
objeto.componerCurso()
#print(objeto.verCursos())
#creamos un for con una variable para que nos murtre la lista 
for cursito in objeto.verCursos():
    print(cursito.getNombre())
