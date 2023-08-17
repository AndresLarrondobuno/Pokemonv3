import pandas as pd
from cargadorDeDatosDePokemons import CargadorDeDatosDePokemons
from randomizador import Randomizador


class ProcesadorDeDatosDePokemons:
    '''
    Procesar datos para que las clases auxiliares como SeleccionadorDePokemons
    tengan un acceso mas legible mediante el uso del objeto pd.DataFrame
    '''

    def construirDataframePokemons(datosFormateadosDePokemons: list) -> pd.DataFrame:
        dataframe = pd.DataFrame(datosFormateadosDePokemons)

        labelsReordenadosParaColumnas = [
            'nombre',
            'indicePokedex',
            'estadisticas',
            'tipos',
            'movimientos',
            'evolucion'
        ]
        
        dataframe = dataframe.reindex(columns=labelsReordenadosParaColumnas)

        return dataframe


    def construirDataframeEvoluciones(datosFormateadosDePokemons: list):
        pass