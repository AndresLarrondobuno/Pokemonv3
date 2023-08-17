from entrenadorPokemon import Jugador, NPC


class Batalla:
    TAMANIO_DE_EQUIPO = 3
    
    #no se si dar el hint como EntrenadorPokemon para ambos participantes de la batalla, creo estar siendo muy especifico
    def __init__(self, jugador: Jugador, entrenadorNPC: NPC): 
        self._jugador = jugador
        self._entrenadorNPC = entrenadorNPC
        self._participantes = [jugador, entrenadorNPC]
        self.asignarOponentes(jugador, entrenadorNPC)
        self._turnoActual = 1
    

    def asignarOponentes(self, jugador: Jugador, entrenadorNPC: NPC):
        jugador._oponente = entrenadorNPC
        entrenadorNPC._oponente = jugador


    def siguienteTurno(self):
        self._turnoActual += 1