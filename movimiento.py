from Tipo import Tipo

class Movimiento:
    def __init__(self, nombre: str, potencia: int, precision: int, tipo: Tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.potencia = potencia
        self.precision = precision
        self.categoriaDeDano = None


    def __repr__(self) -> str:
        return self.nombre