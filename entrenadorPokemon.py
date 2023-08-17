from pokemon import Pokemon
from movimiento import Movimiento

class EntrenadorPokemon:
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


class Jugador(EntrenadorPokemon):
    def __init__(self, nombre: str, pokemons: list[Pokemon]):
        super().__init__(pokemons)
        self.nombre = nombre
    

    def darOrdenDeAtaque(self, pokemon: Pokemon, movimiento: Movimiento):
        pokemonAAtacar = self.getPokemonAAtacar()
        pokemon.atacar(pokemonAAtacar, movimiento)


class NPC(EntrenadorPokemon):
    def __init__(self, pokemons: list[Pokemon]):
        super().__init__(pokemons)
        self.nombre = 'Kevin el NPC'
    

    def darOrdenDeAtaque(self, pokemon: Pokemon, movimiento: Movimiento):
        pokemonAAtacar = self.getPokemonAAtacar()
        pokemon.atacar(pokemonAAtacar, movimiento)
    

    def evaluarEstadoDePokemonEnCombate(self):
        if self._pokemonEnCombate._puntosDeVida <= 0:
            return 'no puede pelear'
        else:
            return 'puede pelear'