from SeleccionadorDePokemons import SeleccionadorDePokemons
from AdministradorDeInterfazDeBatalla import AdministradorDeInterfazDeBatalla
from Entrenador import Jugador, NPC
from Batalla import Batalla
from GeneradorDeValoresAlAzar import GeneradorDeValoresAlAzar

seleccionadorDePokemons = SeleccionadorDePokemons()
equipoJugador = seleccionadorDePokemons.obtenerEquipoPokemon(Batalla.TAMANIO_DE_EQUIPO)
equipoNPC = seleccionadorDePokemons.obtenerEquipoPokemon(Batalla.TAMANIO_DE_EQUIPO)

#instancio al jugador y al npc
jugador = Jugador(equipoJugador)
entrenadorNPC = NPC(equipoNPC)

#instancio la batalla
batalla = Batalla(jugador, entrenadorNPC)

administradorDeInterfazDeBatalla = AdministradorDeInterfazDeBatalla()

### simulo un turno entero ###

#ataque
pokemonEnCombateDeJugador = batalla._jugador._pokemonEnCombate

indiceDeMovimiento = administradorDeInterfazDeBatalla.pedirEleccionDeMovimiento(pokemonEnCombateDeJugador)

movimiento = pokemonEnCombateDeJugador._movimientos[indiceDeMovimiento]

danoCausado = jugador.darOrdenDeAtaque(movimiento)

administradorDeInterfazDeBatalla.anunciarJugada(jugador, movimiento, danoCausado)

#respuesta
movimiento = GeneradorDeValoresAlAzar.obtenerElemento(entrenadorNPC._pokemonEnCombate._movimientos)

danoCausado = entrenadorNPC.darOrdenDeAtaque(movimiento)

administradorDeInterfazDeBatalla.anunciarJugada(entrenadorNPC, movimiento, danoCausado)
