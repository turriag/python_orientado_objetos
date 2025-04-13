class TanqueDeCombustible:
    def __init__(self):  
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible

    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

class Auto():
    def __init__(self, tanque):  
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print(f"El auto se movió {distancia} metros")
        else:
            print("No hay suficiente combustible para moverse esa distancia")

    def obtener_posicion(self):  
        return self.posicion

tanque = TanqueDeCombustible()
mi_auto = Auto(tanque)

print(mi_auto.obtener_posicion())
mi_auto.mover(10)
print(mi_auto.obtener_posicion())
mi_auto.mover(20)
print(mi_auto.obtener_posicion())
mi_auto.mover(60)
print(mi_auto.obtener_posicion())
mi_auto.mover(100)
print(mi_auto.obtener_posicion())
mi_auto.mover(100)