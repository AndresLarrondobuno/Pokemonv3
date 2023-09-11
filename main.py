from GeneradorDeEquipos import GeneradorDeEquipos
from Entrenador import Entrenador
from Batalla import Batalla
from Jugada import Jugada

generadorDeEquipos = GeneradorDeEquipos()
equipoJugadorUno = generadorDeEquipos.obtenerEquipoPokemon(Batalla.TAMANIO_DE_EQUIPO)
equipoJugadorDos = generadorDeEquipos.obtenerEquipoPokemon(Batalla.TAMANIO_DE_EQUIPO)

jugadorUno = Entrenador('elKevin96', equipoJugadorUno)
jugadorDos = Entrenador('Ash', equipoJugadorDos)
batalla = Batalla(jugadorUno, jugadorDos) 

administradorDeInterfazDeBatalla = batalla._administradorDeInterfazDeBatalla 
eleccionDeJugada = administradorDeInterfazDeBatalla.ofrecerEleccionDeJugada()

jugadaDeJugadorUno: Jugada = batalla.obtenerJugada(batalla._jugadorUno, eleccionDeJugada)

batalla.stashearJugada(jugadaDeJugadorUno) 

eleccionDeJugada = administradorDeInterfazDeBatalla.ofrecerEleccionDeJugada()

jugadaDeJugadorDos: Jugada = batalla.obtenerJugada(batalla._jugadorDos, eleccionDeJugada)

batalla.stashearJugada(jugadaDeJugadorDos)

jugadasOrdenadas = batalla.obtenerJugadasOrdenadas(batalla._jugadasAEjecutar)

batalla.ejecutarJugadas(jugadasOrdenadas)