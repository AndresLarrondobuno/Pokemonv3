from termcolor import colored
from Pokemon import Pokemon
from Entrenador import Entrenador
from Movimiento import Movimiento
from Jugada import Jugada, JugadaDeAtaque, JugadaDeCambioDePokemon, JugadaDeUsoDeItem


class AdministradorDeInterfazDeBatalla:

    def __init__(self):
        self.anunciarInicioDeBatalla()

    
    def ofrecerEleccionDeJugada(self) -> int:
        mensaje = 'Elegi una opcion: \n1)Atacar \n2)Cambiar Pokemon \n3)Usar Item \n4)Correr\n'
        eleccionDeJugada = int(input(mensaje))

        while (eleccionDeJugada < 1 or eleccionDeJugada > 4):
            eleccionDeJugada = int(input(mensaje))
        
        return eleccionDeJugada
    

    def ofrecerEleccionDeMovimiento(self, pokemon: Pokemon):
        self.mostrarMovimientos(pokemon)
        eleccion = int(input(f'Elegi el movimiento ingresando su indice: \n'))
        return eleccion - 1
    

    def ofrecerEleccionDePokemon(self, entrenador: Entrenador):
        self.mostrarPokemons(entrenador)
        eleccion = int(input(f'Elegi el pokemon ingresando su indice: \n'))
        return eleccion - 1


    def mostrarMovimientos(self, pokemon: Pokemon):
        print(f'movimientos de {pokemon}: \n')
        for indice, movimiento in enumerate(pokemon._movimientos):
            if movimiento:
                print(f'{indice + 1}) {movimiento} | potencia: {movimiento.potencia} | precision: {movimiento.precision} \n')


    def mostrarPokemons(self, entrenador: Entrenador):
        for indice, pokemon in enumerate(entrenador._pokemons):
            if pokemon._puedePelear:
                print(f'{indice + 1}) {pokemon} \n')


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


    def pedirNombreAJugador(self):
        nombre = input(f'ingresa tu nombre: ')
        print()
        return nombre


    def anunciarJugada(self, jugada: JugadaDeAtaque|JugadaDeCambioDePokemon|JugadaDeUsoDeItem):
        mensaje = jugada.generarMensaje()
        self.colorVerde(mensaje)


    def anunciarMuerte():
        pass