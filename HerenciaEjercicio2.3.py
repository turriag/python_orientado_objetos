"""
# Ejercicio de herencia y uso de super:

Crear un sistema para una escuela. En este sistema, vamos a tener dos clases principales: PERSONA y ESTUDIANTE.
La clase PERSONA tendrá los atributos de nombre y edad y un metodo que imprima el nombre y la edad de la persona.
La clase ESTUDIANTE heredará de la clase PERSONA y tendrá un atributo adicional que será el grado del estudiante.

Deberas utilizar super en el metodo de inicialización (init) para reutilizar el codigo que la clase padre
(PERSONA). Luego crear una intancia de la clase ESTUDIANTE e imprimir sus atributos y utilizar sus metodos
para asegurarte de que todo funcione correctamente.

"""

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

class estudiante(persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)  
        self.grado = grado

    def mostrar_grado(self):
        print(f"Grado: {self.grado}")

estudiante = estudiante("Juan", 20, "10mo")
estudiante.mostrar_datos()
estudiante.mostrar_grado()