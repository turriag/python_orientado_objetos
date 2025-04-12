class persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self,new_nombre):
        self.nombre = new_nombre

dato = persona("Luis",19)

nombre = dato.get_nombre()
print(nombre)


dato.set_nombre("Juan")

nombre = dato.get_nombre()
print(nombre)

