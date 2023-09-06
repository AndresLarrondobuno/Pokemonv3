from Movimiento import Movimiento
from Pokemon import Pokemon
from Entrenador import Entrenador
from Item import Item

class Jugada:
    def __init__(self, entrenador: Entrenador):
        self._entrenador = entrenador
        self._turno = None


    def obtenerInformacionDeJugada(self):
        return
    

    def ejecutar(self):
        return


class JugadaDeAtaque(Jugada):
    def __init__(self, entrenador: Entrenador, movimiento: Movimiento, dano: int, esLetal: bool, esPrimerAtaque: bool):
        super().__init__(entrenador)
        self._movimiento = movimiento
        self._dano = dano
        self._esLetal = esLetal
        self._esPrimerAtaque = esPrimerAtaque
        self._pokemonAAtacar = entrenador.getPokemonAAtacar()


    def obtenerInformacionDeJugada(self):
        return {'dano': self._dano, 'movimiento': self._movimiento, 'esLetal': self._esLetal, 'esPrimerAtaque': self._esPrimerAtaque}


    def ejecutar(self):
        self._entrenador.darOrdenDeAtaque(self._movimiento)
    

    def generarMensaje(self) -> str:
        mensaje = f'''
        {self._entrenador._pokemonEnCombate} ataco a {self._pokemonAAtacar} con {self._movimiento} causando {self._dano}pts de daño.
        '''
        return mensaje


class JugadaDeCambioDePokemon(Jugada):
    def __init__(self, entrenador: Entrenador, pokemonEntrante: Pokemon, pokemonSaliente: Pokemon):
        super().__init__(entrenador)
        self._pokemonEntrante = pokemonEntrante
        self._pokemonSaliente = pokemonSaliente


    def obtenerInformacionDeJugada(self):
        return {'pokemonEntrante': self._pokemonEntrante, 'pokemonSaliente':self._pokemonSaliente}
    

    def generarMensaje(self) -> str:
        mensaje = f'{self._pokemonSaliente} fue retirado del combate. \nes tu turno {self._pokemonEntrante} !!!'
        return mensaje
    

    def ejecutar(self):
        self._entrenador.cambiarDePokemon(self._pokemonEntrante)


class JugadaDeUsoDeItem(Jugada):
    def __init__(self, entrenador: Entrenador, item: Item):
        super().__init__(entrenador)
        self.item = item

    def obtenerInformacionDeJugada(self):
        return {'item': self.item}
    

    def ejecutar(self):
        pass