class Animal():
    def sonido(self):
        pass

class gato(Animal):
    def sonido(self):
        return "Miau"
    

class perro(Animal):
    def sonido(self):
        return "Guau"


def hacer_sonido(animal):
    return animal.sonido()

gato = gato()
perro = perro()    

hacer_sonido(gato)


print(gato.sonido())
print(perro.sonido())

