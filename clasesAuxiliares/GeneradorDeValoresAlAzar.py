import random

class GeneradorDeValoresAlAzar:

    def obtenerNumeroEntero(comienzo: int, fin: int):
        '''incluye ambos extremos'''
        numero = random.randint(comienzo, fin)
        return numero
    

    def obtenerMuestra(poblacion: list, tamanoDeMuestra: int):
        try:
            return random.sample(poblacion, tamanoDeMuestra)
        except ValueError:
            cantidadDeValoresDefaultAAgregar = tamanoDeMuestra - len(poblacion)
            valoresDefault = [None for _ in range(cantidadDeValoresDefaultAAgregar)]
            poblacionRellenadaConValoresDefault = poblacion + valoresDefault
            return poblacionRellenadaConValoresDefault
    

    def obtenerElemento(poblacion: list):
        return random.choice(poblacion)