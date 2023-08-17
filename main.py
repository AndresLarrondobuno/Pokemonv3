from cargadorDeDatosDePokemons import CargadorDeDatosDePokemons
from procesadorDeDatosDePokemons import ProcesadorDeDatosDePokemons
from seleccionadorDePokemons import SeleccionadorDePokemons
from entrenadorPokemon import Jugador, NPC
from pokemon import Pokemon
from batalla import Batalla
from tipo import Tipo
from administradorDeInterfazDeBatalla import AdministradorDeInterfazDeBatalla

import requests
import requests_cache
requests_cache.install_cache('Cache Pokemons Generacion 1')

#llamo a todas las url correspondientes a los pokemons de generacion 1 y formateo los datos para su procesamiento
'''
listaDePokemons = CargadorDeDatosDePokemons.obtenerDatosDePokemonsDeGeneracionUno()

#guardo los datos de los pokemons en un objeto DataFrame, que contiene metodos para procesar los datos
dataFramePokemons = ProcesadorDeDatosDePokemons.construirDataframePokemons(listaDePokemons)

#formo los equipos
equipoJugador = SeleccionadorDePokemons.formarEquipoPokemon(dataFramePokemons, 3)
equipoNPC = SeleccionadorDePokemons.formarEquipoPokemon(dataFramePokemons, 3)

#instancio a los participantes de la batalla
nombreJugador = AdministradorDeInterfazDeBatalla.pedirNombreAJugador()
jugador, oponente = Jugador(nombreJugador, equipoJugador), NPC(equipoNPC)

#instancio la batalla
batalla = Batalla(jugador, oponente)

#simulo un turno entero
pokemonEnCombateDeJugador = batalla._jugador._pokemonEnCombate

pokemonAAtacar = jugador.getPokemonAAtacar()

AdministradorDeInterfazDeBatalla.mostrarMovimientos(pokemonEnCombateDeJugador)

indiceDeMovimiento = AdministradorDeInterfazDeBatalla.pedirEleccionDeMovimiento(pokemonEnCombateDeJugador)

movimiento = pokemonEnCombateDeJugador._movimientos[indiceDeMovimiento]

pokemonEnCombateDeJugador.atacar(movimiento, pokemonAAtacar)
'''

datosEvolucion = CargadorDeDatosDePokemons.obtenerDatosDeEvolucion('pinsir')

print(datosEvolucion)