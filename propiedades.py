class persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def set_nombre(self,new_nombre):
        self.__nombre = new_nombre
    
    @nombre.deleter
    def nombre(self):
        del self.__nombre

dato = persona("Luis",19)

nombre = dato.nombre
print(nombre)   

dato.set_nombre = "Juan"
print(nombre)

del dato.nombre 

print("esto ronpe la cabeza del programa")
