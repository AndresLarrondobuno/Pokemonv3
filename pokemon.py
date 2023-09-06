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
        self._puedePelear = True


    def __repr__(self) -> str:
        return self._nombre
    

    def setVida(self, dano: int):
        self._puntosDeVida -= dano


    def atacar(self, pokemonAAtacar: 'Pokemon', movimiento: Movimiento):
        dano = self.calcularDano(pokemonAAtacar, movimiento)
        pokemonAAtacar.setVida(dano)
    

    def calcularDano(self, pokemonAAtacar: 'Pokemon', movimiento) -> int:
        if movimiento.potencia:
            return self._ataqueBase + movimiento.potencia - pokemonAAtacar._defensaBase//2
        else:
            return 0
    

    def atacaPrimero(self, pokemonAAtacar: 'Pokemon') -> bool:
        return self._velocidadBase > pokemonAAtacar._velocidadBase
    

    def ataqueEsLetal(self, pokemonAAtacar: 'Pokemon', dano: int) -> bool:
        return True if dano >= pokemonAAtacar._puntosDeVida else False


    def puedePelear(self) -> bool:
        return True if self._puntosDeVida > 0 else False
    

    def obtenerInformacionDeAtaque(self, pokemonAAtacar: 'Pokemon', movimiento: Movimiento) -> dict:
        dano = self.calcularDano(pokemonAAtacar, movimiento)
        atacaPrimero = self.atacaPrimero(pokemonAAtacar)
        esLetal = self.ataqueEsLetal(pokemonAAtacar, dano)
        return {'dano': dano, 'esLetal': esLetal, 'atacaPrimero': atacaPrimero}


    def evolucionar(self, evolucion: 'Pokemon'):
        self._nombre = evolucion._nombre
        self._tipos = [tipo for tipo in evolucion._tipos]
        self._movimientos = evolucion._movimientos
        self._estadisticas = evolucion._estadisticas