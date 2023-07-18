class persona:
    def __init__(self, nombre, documento):
        self.__nombre = nombre
        self.__documento = documento
        self.__cursos = []
        
    def setnombre(self, nombre):
        self.__nombre = nombre 
    
    
    def getnombre(self):
        return self.__nombre

    def setdocumento(self, documento):
        self.__documento = documento 
        
        
    def getdocumento(self):
        return self.__documento
    
    def setcursos(self, cursos):
        self.__cursos.append(cursos)
        
    def getcursos(self):
        return self.__cursos
    
    def deletecursos(self, cursos):
        if cursos in self.__cursos:
            self.__cursos.remove(cursos)
        else:
            print('no esta en la lista ')

