from cargadorDeDatos import CargadorDeDatos
from administradorDeBaseDeDatos import AdministradorDeBaseDeDatos
from seleccionadorDePokemons import SeleccionadorDePokemons
from entrenador import Jugador, NPC
from pokemon import Pokemon
from batalla import Batalla
from tipo import Tipo
from administradorDeInterfazDeBatalla import AdministradorDeInterfazDeBatalla
import os, requests_cache, requests
requests_cache.install_cache('Cache Pokemons Generacion 1')

administradorDeBaseDeDatos = AdministradorDeBaseDeDatos('pokemon')

'''
#INSERCIONES A DB
administradorDeBaseDeDatos.insertarPokemons()
administradorDeBaseDeDatos.insertarMovimientos()
administradorDeBaseDeDatos.crearTablaMovimientosAdquiribles()
administradorDeBaseDeDatos.insertarFilasAMovimientosAdquiribles()
'''

equipo = administradorDeBaseDeDatos.obtenerEquipoPokemon(3)
print(equipo)


'''
nombreJugador = AdministradorDeInterfazDeBatalla.pedirNombreAJugador()

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
