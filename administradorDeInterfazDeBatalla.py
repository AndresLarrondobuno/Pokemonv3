from termcolor import colored
from Pokemon import Pokemon
from Entrenador import Entrenador
from Movimiento import Movimiento

class AdministradorDeInterfazDeBatalla:

    def __init__(self):
        self.anunciarInicioDeBatalla()


    def colorRojo(self, texto: str):
        texto = colored(texto, 'red')
        print(texto)


    def colorVerde(self, texto: str):
        texto = colored(texto, 'green')
        print(texto)


    def anunciarInicioDeBatalla(self):
        self.colorRojo(f'Comenzo la pelea')


    def anunciarTurno(self, turno: int):
        print(f'Turno numero: {turno}\n')
    

    def pedirEleccionDeMovimiento(self, pokemon: Pokemon):
        self.mostrarMovimientos(pokemon)
        eleccion = int(input(f'Elegi el movimiento ingresando su indice: '))
        print()
        return eleccion - 1


    def mostrarMovimientos(self, pokemon: Pokemon):
        for indice, movimiento in enumerate(pokemon._movimientos):
            if movimiento:
                print(f'{indice + 1}) {movimiento} | potencia: {movimiento.potencia} | precision: {movimiento.precision} \n')


    def pedirNombreAJugador(self):
        nombre = input(f'ingresa tu nombre: ')
        print()
        return nombre


    def anunciarJugada(self, jugador: Entrenador, movimiento: Movimiento , dano: int):
        pokemonAAtacar = jugador.getPokemonAAtacar()
        self.colorRojo(f'{jugador._pokemonEnCombate} ataco a {pokemonAAtacar} con {movimiento} causando {dano}pts de daño.')


    def anunciarMuerte():
        pass