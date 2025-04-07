class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"Llamando desde el {self.marca} {self.modelo}...")

    def cortar_llamada(self):
        print(f"Cortando llamada en el {self.marca} {self.modelo}...")

celular1 = Celular("Samsung", "Galaxy S21", "108 MP")
celular2 = Celular("Apple", "iPhone 13", "48 MP")

print(f"Celular 1: {celular1.marca} {celular1.modelo}, Cámara: {celular1.camara}")
print(f"Celular 2: {celular2.marca} {celular2.modelo}, Cámara: {celular2.camara}")

celular1.llamar()
celular2.cortar_llamada()
