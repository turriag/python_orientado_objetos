class persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print(f"{self.nombre} está hablando.")
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        print(f"{self.nombre} es un artista y su habilidad es {self.habilidad}.")

class empleadoArtista(persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def present(self):
        return f"{self.nombre} trabaja en {self.empresa} como artista y gana {self.salario}."
    
roberto = empleadoArtista("Luis", 19, "Colombino", "cantar", 50000, "Programador")
roberto.hablar()
roberto.mostrar_habilidad()
print(roberto.present())
