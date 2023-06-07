class Empleado:
    def __into__ (self, nombre, cargo, salario):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario
    def setnombre (self, nombre):
        self.__nombre=nombre
    def getnombre(self):
        return self.__nombre
    def setcargo (self, cargo):
        self.__cargo=cargo
    def getcargo(self):
        return self.__cargo
    def setsalario (self, salario):
        self.__salario=salario
    def getnombre(self):
        return self.__salario
    def calculoxhora(salario):
        m=salario/30
        m=m/8
        return m 
    def ipc (salario):
        if salario>1160000:
            s=salario*19/100
            s=s+salario
        return s 
        else:
            s=salario*16/100
            s=s+salario
        return s
        
ob1=Empleado('juan', axu, 1160000)
print(type (ob1))
print(ob1.getnombre())
print(ob1.gecargo())
print(ob1.getsalario())
print(f'la hora se lo pagan a :{calculoxhora(salario)}')
