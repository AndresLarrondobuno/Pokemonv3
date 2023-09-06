from Pokemon import Pokemon
from Movimiento import Movimiento
from clasesAuxiliares.GeneradorDeValoresAlAzar import GeneradorDeValoresAlAzar
from Item import Item


class Entrenador:
    '''
    Contiene las propiedades de un EntrenadorPokemon
    Contiene metodos para controlar los estados y acciones de objetos Pokemon
    '''

    def __init__(self, nombre: str, pokemons: list[Pokemon]):
        self._pokemons = pokemons
        self._pokemonEnCombate = self._pokemons[0]
        self._oponente = None
        self.nombre = nombre
    

    def __repr__(self) -> str:
        return self.nombre


    def darOrdenDeAtaque(self, movimiento: Movimiento):
        pokemonAAtacar = self.getPokemonAAtacar()
        self._pokemonEnCombate.atacar(pokemonAAtacar, movimiento)


    def cambiarDePokemon(self, pokemonEntrante: Pokemon):
        pokemonSaliente = self._pokemonEnCombate
        pokemonSaliente._enCombate = False
        pokemonEntrante._enCombate = True


    def usarItem(self, item: Item):
        pass


    def getPokemonAAtacar(self) -> Pokemon:
        pokemonAAtacar = self._oponente._pokemonEnCombate
        return pokemonAAtacar

    

