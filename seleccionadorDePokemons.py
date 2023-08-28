from generadorDeValoresAlAzar import GeneradorDeValoresAlAzar
from pokemon import Pokemon
from movimiento import Movimiento
import pandas as pd


class SeleccionadorDePokemons:
    '''
    1)Construye las intancias de pokemons en base a la informacion del dataframe
    que contiene los datos de pokemons 
    2)Forma los equipos para los participantes de la batalla
    '''

    def obtenerEquipoPokemon() -> list[Pokemon]:
        equipoPokemon = []
        for datosPokemon in dataFrameEquipoPokemon.itertuples():
            pokemon = SeleccionadorDePokemons.obtenerPokemon(datosPokemon)
            equipoPokemon.append(pokemon)
        
        return equipoPokemon


    def obtenerPokemon(datosPokemon) -> Pokemon: #el input es el objeto devuelvo por el query
        nombre = ''
        tipos = ''
        movimientos = ''
        estadisticas = ''

        pokemon = Pokemon(nombre=nombre,
                          tipos=tipos,
                          movimientos=movimientos,
                          estadisticas=estadisticas)

        return pokemon


    def obtenerMovimientos(datosMovimientos):
        movimientos = []
        cantidadDeMovimientos = 4
        for indice in range(cantidadDeMovimientos):
            nombre = datosMovimientos[indice]['nombre']
            tipo = datosMovimientos[indice]['tipo']
            potencia = datosMovimientos[indice]['potencia']
            precision = datosMovimientos[indice]['precision']
            movimiento = Movimiento(nombre, tipo, potencia, precision)
            movimientos.append(movimiento)
        return movimientos
    

    def obtenerEvolucionesDe(dataframe: pd.DataFrame, nombreDePokemon: str) -> list:
        idsDeEvoluciones = dataframe.loc['idsDeEvoluciones']