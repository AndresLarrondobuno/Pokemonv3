from Pokemon import Pokemon
from Movimiento import Movimiento
from GeneradorDeValoresAlAzar import GeneradorDeValoresAlAzar

class Entrenador:
    '''
    Contiene las propiedades de un EntrenadorPokemon
    Contiene metodos para controlar los estados y acciones de objetos Pokemon
    '''

    def __init__(self, pokemons: list[Pokemon]):
        self._pokemons = pokemons
        self._pokemonEnCombate = self._pokemons[0]
        self._oponente = None
        self.nombre = None
    

    def __repr__(self) -> str:
        return self.nombre


    def cambiarDePokemon(self, indicePokemonEnEquipo: int):
        indiceCorregidoParaUbicarPokemonEnEquipo = indicePokemonEnEquipo + 1
        self._pokemonEnCombate = self._pokemons[indiceCorregidoParaUbicarPokemonEnEquipo]


    def getPokemonAAtacar(self) -> Pokemon:
        pokemonAAtacar = self._oponente._pokemonEnCombate
        return pokemonAAtacar


class Jugador(Entrenador):

    def __init__(self, pokemons: list[Pokemon], nombre: str = 'Ash'):
        super().__init__(pokemons)
        self.nombre = nombre
    

    def darOrdenDeAtaque(self, movimiento: Movimiento):
        pokemonAAtacar = self.getPokemonAAtacar()
        dano = self._pokemonEnCombate.atacar(pokemonAAtacar, movimiento)
        return dano


class NPC(Entrenador):

    def __init__(self, pokemons: list[Pokemon], nombre = 'Kevin el NPC'):
        super().__init__(pokemons)
        self.nombre = nombre
    

    def darOrdenDeAtaque(self, movimiento: Movimiento):
        pokemonAAtacar = self.getPokemonAAtacar()
        dano = self._pokemonEnCombate.atacar(pokemonAAtacar, movimiento)
        return dano
