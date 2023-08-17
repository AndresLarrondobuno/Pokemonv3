import random

class Randomizador:

    def obtenerNumeroEntero(comienzo: int, fin: int):
        numero = random.randint(comienzo, fin)
        return numero
    

    def obtenerMuestra(poblacion: list, tamanoDeMuestra: int):
        return random.sample(poblacion, tamanoDeMuestra)
    

    def obtenerElemento(poblacion: list):
        return random.choice(poblacion)