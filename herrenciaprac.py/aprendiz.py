
from objetos.persona import persona
from persona import *


class Aprendiz(persona):
    def __init__(self, nombre, documento, formacion, ficha):
        Persona.__init__(nombre, documento)
        self.__formacion = formacion
        self.__ficha = ficha 
        self.__cursos=[]
    def agregarcursos(self, cursor):
        self.__cursos.append(cursor)