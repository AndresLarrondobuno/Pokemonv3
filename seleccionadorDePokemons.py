from randomizador import Randomizador
from pokemon import Pokemon
from movimiento import Movimiento
import pandas as pd


class SeleccionadorDePokemons:
    '''
    1)Construye las intancias de pokemons en base a la informacion del dataframe
    que contiene los datos de pokemons 
    2)Forma los equipos para los participantes de la batalla
    '''

    def formarEquipoPokemon(dataFramePokemons: pd.DataFrame, tamanoDeEquipo: int) -> list[Pokemon]:
        cantidadDeFilas = len(dataFramePokemons) - 1
        indicesParaLocalizarPokemons = [Randomizador.obtenerNumeroEntero(1, cantidadDeFilas) for n in range(tamanoDeEquipo)]
        dataFrameEquipo = dataFramePokemons.iloc[indicesParaLocalizarPokemons]

        equipo = list()
        for datosPokemon in dataFrameEquipo.itertuples(index=False):
            #aca agregar evolucion = SeleccionadorDePokemons.obtenerEvolucion()
            #hay que hacer el mismo recorrido que hice con los demas datos

            pokemon = SeleccionadorDePokemons.obtenerPokemon(datosPokemon)
            equipo.append(pokemon)

        return equipo


    def obtenerPokemon(datosPokemon) -> Pokemon:
        #se accede a los atributos de objetos 'namedtuple' que genera pandas
        #para instanciar los Pokemons a partir de las filas del dataFramePokemons
        print(datosPokemon.evolucion)
        if datosPokemon.evolucion:
            evolucion = SeleccionadorDePokemons.obtenerPokemon(datosPokemon.evolucion)

        nombre = datosPokemon.nombre
        tipos = datosPokemon.tipos
        movimientos = SeleccionadorDePokemons.obtenerMovimientos(datosPokemon.movimientos)
        estadisticas = datosPokemon.estadisticas

        pokemon = Pokemon(nombre=nombre,
                          tipos=tipos,
                          movimientos=movimientos,
                          estadisticas=estadisticas,
                          evolucion=evolucion)

        return pokemon


    def obtenerMovimientos(datosMovimientos):
#refactorizar para que se recorra datosMovimientos y se acceda con la llave correspondiente a cada diccionario de datos
        movimientos = []
        for indice, datosMovimiento in enumerate(datosMovimientos):
            nombre = datosMovimientos[indice]['nombre']
            tipo = datosMovimientos[indice]['tipo']
            potencia = datosMovimientos[indice]['potencia']
            precision = datosMovimientos[indice]['precision']
            movimiento = Movimiento(nombre, tipo, potencia, precision)
            movimientos.append(movimiento)
        return movimientos
    

    
            

