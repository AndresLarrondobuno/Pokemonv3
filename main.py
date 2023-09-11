from GeneradorDeEquipos import GeneradorDeEquipos
from Entrenador import Entrenador
from Batalla import Batalla

generadorDeEquipos = GeneradorDeEquipos()
equipoJugadorUno = generadorDeEquipos.obtenerEquipoPokemonAleatorio(3)
equipoJugadorDos = generadorDeEquipos.obtenerEquipoPokemonAleatorio(3)

jugadorUno = Entrenador('elKevin96', equipoJugadorUno)
jugadorDos = Entrenador('Ash', equipoJugadorDos)
batalla = Batalla(jugadorUno, jugadorDos)

administradorDeInterfazDeBatalla = batalla._administradorDeInterfazDeBatalla
eleccionDeJugada = administradorDeInterfazDeBatalla.ofrecerEleccionDeJugada()

jugadaDeJugadorUno = batalla.obtenerJugada(batalla._jugadorUno, eleccionDeJugada)

batalla.stashearJugada(jugadaDeJugadorUno)

eleccionDeJugada = administradorDeInterfazDeBatalla.ofrecerEleccionDeJugada()

jugadaDeJugadorDos = batalla.obtenerJugada(batalla._jugadorDos, eleccionDeJugada)

batalla.stashearJugada(jugadaDeJugadorDos)

jugadasOrdenadas = batalla.obtenerJugadasOrdenadas(batalla._jugadasAEjecutar)

batalla.ejecutarJugadas(jugadasOrdenadas)