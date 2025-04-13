"""
# Chatbot analizador de sentimientos

En este proyecto, podras desarrollar un chatbot en python, que nos pida que le digamos algo y tome eso que le decimos
analice el sentimiento y nos responda cual es el sentimiento.

Este proyecto te dara la oportunidad de trabajar con varios aspectos de la programacion orientada a objetos (poo),
modulos,API,analisis de datos, etc...

""" 
from textblob import TextBlob

class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color, self.nombre)

class AnalizadorDeSentimientos:
    def __init__(self, rangos):
        self.rangos = rangos

    def analizar_sentimiento(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <= rango[1]:
                return sentimiento
        return Sentimiento("Muy negativo", "31")

rangos = [
    ((-0.6, -0.3), Sentimiento("negativo", "31")),
    ((-0.3, -0.1), Sentimiento("algo negativo", "31")),
    ((-0.1, 0.1), Sentimiento("neutral", "33")),
    ((0.1, 0.4), Sentimiento("algo positivo", "32")),
    ((0.4, 0.9), Sentimiento("positivo", "32")),
    ((0.9, 1.1), Sentimiento("muy positivo", "32"))  # ampliamos a 1.1 por seguridad
]

analizador = AnalizadorDeSentimientos(rangos)

while True:
    user_prompt = input("\x1b[1;33m" + "\nDecime Algo: " + "\x1b[0;37m")
    blob = TextBlob(user_prompt)
    polaridad = blob.sentiment.polarity

    sentimiento = analizador.analizar_sentimiento(polaridad)
    print(sentimiento)
