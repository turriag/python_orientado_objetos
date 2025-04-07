class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"{self.nombre} está estudiando...")


class PersonaApp:
    def __init__(self):
        self.estudiante = None

    def iniciar(self):
        self.obtener_datos_estudiante()
        self.mostrar_datos_estudiante()
        self.menu_interactivo()

    def obtener_datos_estudiante(self):
        nombre = input("Ingrese por favor su nombre: ")
        edad = input("Ingrese por favor su edad: ")
        grado = input("Por favor, ingrese su grado: ")
        self.estudiante = Estudiante(nombre, edad, grado)

    def mostrar_datos_estudiante(self):
        print(f"""
    DATOS DEL ESTUDIANTE
    Nombre: {self.estudiante.nombre}
    Edad: {self.estudiante.edad}
    Grado: {self.estudiante.grado}
    """)

    def menu_interactivo(self):
        while True:
            comando = input("Ingrese 'estudiar' para que el estudiante estudie o 'salir' para terminar: ").lower()
            if comando == "estudiar":
                self.estudiante.estudiar()
            elif comando == "salir":
                print("Saliendo del programa...")
                break
            else:
                print("Comando no reconocido. Intente nuevamente.")


if __name__ == "__main__":
    app = PersonaApp()
    app.iniciar()
