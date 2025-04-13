class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'Persona: {self.nombre}, Edad: {self.edad}'
    
    def __repr__(self):
        return f'Persona({self.nombre}, {self.edad})'
    
    def __add__(self,other):
        nuevo_valor = self.edad + other.edad
        return Persona(self.nombre+other.nombre, nuevo_valor)

luis = Persona("Luis",19)
juan = Persona("Juan",25)

nueva_persona = luis + juan
print(nueva_persona.edad)