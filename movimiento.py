from tipo import Tipo

class Movimiento:
    def __init__(self, nombre: str, tipo: Tipo, potencia: int, precision: int):
        self.nombre = nombre
        self.tipo = tipo
        self.potencia = potencia
        self.precision = precision
    

    def __repr__(self) -> str:
        return self.nombre
