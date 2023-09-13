from Entrenador import Entrenador
from Evento import AdministradorDeInterfazDeBatalla
from Jugada import Jugada, JugadaDeAtaque, JugadaDeCambioDePokemon, JugadaDeUsoDeItem
from Arbitro import Arbitro

class Batalla:
    
    def __init__(self, jugadorUno: Entrenador, jugadorDos: Entrenador):
        self._jugadas = []
        self._jugadorUno, self._jugadorDos = jugadorUno, jugadorDos
        self._participantes = (jugadorUno, jugadorDos)
        self.asignarOponentes(jugadorUno, jugadorDos)
        self._turnoActual = 1
        self._administradorDeInterfazDeBatalla = AdministradorDeInterfazDeBatalla()
        self._jugadaAEjecutarDeJugadorUno: Jugada = None
        self._jugadaAEjecutarDeJugadorDos: Jugada = None
        self._jugadasAEjecutar = []
        self._arbitro = Arbitro()


    def asignarOponentes(self, jugadorUno: Entrenador, jugadorDos: Entrenador):
        jugadorUno._oponente = jugadorDos
        jugadorDos._oponente = jugadorUno


    def siguienteTurno(self):
        self._turnoActual += 1


    def obtenerJugada(self, jugador: Entrenador, eleccion: int) -> Jugada:
        ataqueFueElegido = eleccion == 1
        cambioFueElegido = eleccion == 2
        itemFueElegido = eleccion == 3

        if ataqueFueElegido:
            pokemonEnCombateDeJugador = jugador._pokemonEnCombate
            indiceDeMovimiento = self._administradorDeInterfazDeBatalla.ofrecerEleccionDeMovimiento(pokemonEnCombateDeJugador)
            movimiento = pokemonEnCombateDeJugador._movimientos[indiceDeMovimiento]
            pokemonAAtacar = jugador.getPokemonAAtacar()
            informacionAtaque = jugador._pokemonEnCombate.obtenerInformacionDeAtaque(pokemonAAtacar, movimiento)
            return JugadaDeAtaque(jugador, movimiento, informacionAtaque['dano'], informacionAtaque['esLetal'], informacionAtaque['atacaPrimero'])
        elif cambioFueElegido:
            indiceDePokemonEntrante = self._administradorDeInterfazDeBatalla.ofrecerEleccionDePokemon(jugador)
            pokemonEntrante = jugador._pokemons[indiceDePokemonEntrante]
            return JugadaDeCambioDePokemon(jugador, pokemonEntrante, jugador._pokemonEnCombate)
        elif itemFueElegido:
            print('eleccion: Item')


    def obtenerVelocidad(self, jugada: Jugada) -> int:
        return jugada._entrenador._pokemonEnCombate._velocidadBase

    
    def obtenerJugadasOrdenadas(self, jugadas: list[Jugada]) -> list[Jugada]:
        return sorted(jugadas, key=self.obtenerVelocidad, reverse=True)


    def ejecutarJugada(self, jugada: JugadaDeAtaque|JugadaDeCambioDePokemon|JugadaDeUsoDeItem):
        jugada.ejecutar()


    def ejecutarJugadas(self, jugadas: list[Jugada]):
        for jugada in jugadas:
            print(f'ejecutando jugada de {jugada._entrenador}...')
            self.ejecutarJugada(jugada)
            self._administradorDeInterfazDeBatalla.anunciarJugada(jugada)
            self.guardarJugada(jugada)
            if self._arbitro.esLetal(jugada):
                print(f'{jugada._pokemonAAtacar} fue vencido.')
                return


    def guardarJugada(self, jugada: Jugada):
        self._jugadas.append(jugada)


    def stashearJugada(self, jugada: Jugada):
        self._jugadasAEjecutar.append(jugada)
        self._arbitro._jugadas.append(jugada)