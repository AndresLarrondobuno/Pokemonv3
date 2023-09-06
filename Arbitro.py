from Jugada import Jugada, JugadaDeAtaque, JugadaDeCambioDePokemon, JugadaDeUsoDeItem

class Arbitro:
    def __init__(self):
        self._jugadas = []
        self._turno = None


    def esLetal(self, jugada: Jugada) -> bool:
        esElPrimerAtaque = jugada is self._jugadas[0]
        esJugadaDeAtaque = type(jugada) == JugadaDeAtaque
        if esJugadaDeAtaque:
            if jugada._esLetal and esElPrimerAtaque:
                return True