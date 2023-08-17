from batalla import Batalla
from pokemon import Pokemon

class AdministradorDeInterfazDeBatalla:

    def anunciarInicioDeBatalla(batalla: Batalla):
        jugador, npc = batalla._participantes
        print(f'Comenzo la pelea entre {jugador} y {npc}')


    def anunciarTurno(turno: int):
        print(f'Turno numero: {turno}')
        print()
    

    def pedirEleccionDeMovimiento(pokemon: Pokemon):
        eleccion = int(input(f'Elegi el movimiento ingresando su indice: '))
        print()
        return eleccion - 1


    def mostrarMovimientos(pokemon: Pokemon):
        for indice, movimiento in enumerate(pokemon._movimientos):
            print(f'{indice + 1}) {movimiento.nombre} | potencia: {movimiento.potencia} | precision: {movimiento.precision}')
        print()


    def pedirNombreAJugador():
        nombre = input(f'ingresa tu nombre: ')
        print()
        return nombre


    def anunciarJugada():
        pass


    def anunciarMuerte():
        pass