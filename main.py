import time
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

'''
administradorDeBaseDeDatos = AdministradorDeBaseDeDatos('pokemon')
administradorDeBaseDeDatos.insertarPokemons()
administradorDeBaseDeDatos.insertarMovimientos()
administradorDeBaseDeDatos.crearTablaMovimientosAdquiribles()
administradorDeBaseDeDatos.insertarCombinacionDeIdsATablaMovimientosAdquiribles(1, 8)
'''
idsMovimientos = dict()
for id in range(1, 11):
    inicio = time.time()
    print(f'iniciando id: {id} \n')

    idsDeMovimientos = CargadorDeDatos.cargarMovimientosAdquiriblesDe(id)
    print(idsDeMovimientos)
    print(f'{len(idsDeMovimientos)}')

    fin = time.time()
    print(f'{fin-inicio} s de ejecucion')
    print('\n - - - - - - - - \n')


'''
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