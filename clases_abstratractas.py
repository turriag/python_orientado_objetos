from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self):
        print(f"Estoy trabajando en: {self.actividad}")

luis = Estudiante("Luis",19,"Masculino","Python")
dalto = Trabajador("juan",25,"Masculino","programacion")

dalto.presentarse()
dalto.hacer_actividad()

luis.presentarse()
luis.hacer_actividad()

