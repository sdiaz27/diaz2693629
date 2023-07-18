#realizamos la importacion de las clases pensona y curso
from Persona import *
from Curso import *
#cramos la clase aprendiz
class Aprendiz(Persona):
    #cramos un contenedor con sus carateres 
    def __init__(self,nombre,documento,formacion,ficha):
        #llamamos lao caracteres de la clase persona
        Persona.__init__(self,nombre,documento)
        #damos los a describir los agumento para que sena guardados en uan parte de  la memoria 
        self.__formacion=formacion
        self.__ficha=ficha
        #creamos una lista donde iran los corsos 
        self.__cursos=[]
    #realizamos un getter de los cursos 
    def agregarCurso(self,curso):
        #desimos que no retorne el resultado para nosostros poderelo manejar 
        self.__cursos.append(curso)
    #cramos la composicion  para que el usuario registe sues cursos por medio de la consola 
    def componerCurso(self):
        nombreCurso=input('Ingrese nombre del curso')
        tipoCurso=input('Ingrese tipo del curso')
        objcurso=Curso(nombreCurso,tipoCurso)
        self.__cursos.append(objcurso)
    #es para que nos mueste la lista 
    def verCursos(self):
        return self.__cursos