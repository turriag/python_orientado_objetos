# class Diccionario:
#     def verificar_palabras(self, palabra):
#         #logica para verificar si la palabra existe en el diccionario
#         pass

# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()

#     def Corregir(self, texto):
#         #usamos el diccionario para corregir el texto
#         pass

from abc import ABC, abstractmethod

class  VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Lógica para verificar si la palabra existe en el diccionario
        pass

class CorrectorOrtografico:
    def __init__(self, verificador: VerificadorOrtografico):
        self.verificador = verificador

    def corregir(self, texto):
        # Usamos el verificador para corregir el texto
        pass 