from movimiento import Movimiento
from tipo import Tipo

class Pokemon:
    '''
    Contiene las acciones y atributos de los pokemons
    '''

    def __init__(self, nombre: str, tipos: list[Tipo], movimientos: list[Movimiento], estadisticas: dict[str,int]):
        self._nombre = nombre
        self._tipos = tipos
        self._estadisticas = estadisticas
        self._movimientos = movimientos
        self._puntosDeVida = estadisticas['hp']
        self._vidaTotal = estadisticas['hp']
        self._ataqueBase = estadisticas['attack']
        self._defensaBase = estadisticas['defense']
        self._velocidadBase = estadisticas['speed']
        self._enCombate = False
   

    def __repr__(self) -> str:
        return self._nombre


    def atacar(self, movimiento: Movimiento, pokemonAAtacar: 'Pokemon'):
        danio = self._ataqueBase + movimiento.potencia
        pokemonAAtacar._puntosDeVida -= danio
    

    def evolucionar(self, evolucion: 'Pokemon'):
        self._nombre = evolucion._nombre
        self._tipos = [tipo for tipo in evolucion._tipos]
        self._movimientos = evolucion._movimientos
        self._estadisticas = evolucion._estadisticas
