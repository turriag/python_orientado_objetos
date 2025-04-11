"""
Imagina que estas modelando animales en un zoologico. Crear tres clases: "animales", "mamiferos" y "aves".
La clase "animal" debe tener un metodo llamado "comer". La clase "mamifero" debe tener un metodo llamado "amamantar"
y la clase "ave" un metodo llamado "volar".

Ahora, crear una clase "murcielago" que herede de "mamifero" y "ave", en ese orden, y por lo tanto debe ser capaz 
de "amamantar" y "volar", ademas de "comer".

Finalmente, juega con el orden de la herencia de la clase "murcielago" y observa como cambia el MRO y el comportamiento 
de los metodos al usar super().

"""

class animal:
    def comer(self):
        print("El animal está comiendo.")

class Ave(animal):
    def volar(self):
        print("El ave está volando.")

class Mamifero(animal):
    def amamantar(self):
        print("El mamífero está amamantando.")

class Murcielago(Mamifero, Ave):
    pass

Murcielago = Murcielago()

Murcielago.comer()
Murcielago.volar()
Murcielago.amamantar()
