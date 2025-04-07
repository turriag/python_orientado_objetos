class persona:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"{self.nombre} está estudiando...")

nombre = input("Ingrese por favor su nombre: ")
edad = input("Ingrese por favor su edad: ")
grado = input("Por favor, ingrese su grado: ")

Estudiante = persona(nombre, edad, grado)

print(f"""
DATOS DEL ESTUDIANTE
Nombre: {Estudiante.nombre}
Edad: {Estudiante.edad}
Grado: {Estudiante.grado}
""")

while True:
    estudiar = input("Ingrese 'estudiar' para que el estudiante estudie: ")
    if estudiar.lower() == "estudiar":
        Estudiante.estudiar()
    else:
        print("Comando no reconocido. Intente nuevamente.")

    break

    