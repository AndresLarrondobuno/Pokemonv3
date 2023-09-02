from Entrenador import Jugador, NPC
from AdministradorDeInterfazDeBatalla import AdministradorDeInterfazDeBatalla

class Batalla:
    TAMANIO_DE_EQUIPO = 3
    
    def __init__(self, jugador: Jugador, entrenadorNPC: NPC):
        self._jugador = jugador
        self._entrenadorNPC = entrenadorNPC
        self._participantes = [jugador, entrenadorNPC]
        self.asignarOponentes(jugador, entrenadorNPC)
        self._turnoActual = 1
        #self._administradorDeInterfazDeBatalla = AdministradorDeInterfazDeBatalla()

    def asignarOponentes(self, jugador: Jugador, entrenadorNPC: NPC):
        jugador._oponente = entrenadorNPC
        entrenadorNPC._oponente = jugador


    def siguienteTurno(self):
        self._turnoActual += 1