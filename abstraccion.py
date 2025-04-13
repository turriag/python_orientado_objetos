class auto():
    def __init__(self):
        self.estado = "apagado"

    def encender(self):
        self.estado = "encendido"
        print("El auto está encendido")
    
    def conducir(self):
        if self.estado == "apagado":
            self.encender()
            print("El auto está en movimiento")
mi_auto = auto()
mi_auto.conducir()