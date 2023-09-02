from Movimiento import Movimiento
from Tipo import Tipo

class Pokemon:
    '''
    Contiene las acciones y atributos de los pokemons
    '''

    def __init__(self, nombre: str, tipos: list[Tipo], movimientos: list[Movimiento], estadisticas: dict[str,int]):
        self._nombre = nombre
        self._tipos = tipos
        self._estadisticas = estadisticas
        self._movimientos = movimientos
        self._puntosDeVida = estadisticas['vida']
        self._vidaTotal = estadisticas['vida']
        self._ataqueBase = estadisticas['ataque']
        self._defensaBase = estadisticas['defensa']
        self._ataqueEspecialBase = estadisticas['ataque-especial']
        self._defensaEspecialBase = estadisticas['defensa-especial']
        self._velocidadBase = estadisticas['velocidad']
        self._precision = 100
        self._evasion = 100
        self._enCombate = False


    def __repr__(self) -> str:
        return self._nombre


    def atacar(self, pokemonAAtacar: 'Pokemon', movimiento: Movimiento):
        if movimiento.potencia:
            danio = self._ataqueBase + movimiento.potencia - pokemonAAtacar._defensaBase//2
        else:
            return 0
        pokemonAAtacar._puntosDeVida -= danio
        return danio


    def puedePelear(self):
        return True if self._puntosDeVida > 0 else False


    def evolucionar(self, evolucion: 'Pokemon'):
        self._nombre = evolucion._nombre
        self._tipos = [tipo for tipo in evolucion._tipos]
        self._movimientos = evolucion._movimientos
        self._estadisticas = evolucion._estadisticas