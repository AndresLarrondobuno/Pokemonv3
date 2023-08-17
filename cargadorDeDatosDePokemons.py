import sys
import os
from randomizador import Randomizador
import requests

sys.stdout.reconfigure(encoding='utf-8')

URL_POKEMONS = f"https://pokeapi.co/api/v2/pokemon/"
URL_ESPECIES_POKEMON = 'https://pokeapi.co/api/v2/pokemon-species/'
URL_CADENA_EVOLUTIVA = 'https://pokeapi.co/api/v2/evolution-chain/'
URL_TIPOS = f"https://pokeapi.co/api/v2/type/"
URL_MOVIMIENTOS = f"https://pokeapi.co/api/v2/move/"


class CargadorDeDatosDePokemons:
    '''
    Trae desde pokeAPI al programa la informacion de los pokemons en formato JSON 
    y la formatea para su posterior procesamiento (a cargo de ProcesadorDeDatosDePokemons)
    '''

    def obtenerDatosDePokemonPorId(id: int) -> dict: #se obtienen los datos del pokemon de la respuesta de la API directamente
        response = requests.get(os.path.join(URL_POKEMONS, str(id)))
        datosPokemon = response.json()
        return datosPokemon


    def obtenerDatosDePokemonsDeGeneracionUno() -> list:
        datosFormateadosDePokemons = list()
        indicesDePokedexDeGeneracionUno = range(1, 152)

        for id in indicesDePokedexDeGeneracionUno:
            datosDelPokemon = CargadorDeDatosDePokemons.obtenerDatosDePokemonPorId(id)
            indicePokedex = datosDelPokemon['id']
            nombre = datosDelPokemon['name']
            estadisticas = CargadorDeDatosDePokemons.obtenerDatosDeEstadisticas(datosDelPokemon)
            tipos = CargadorDeDatosDePokemons.obtenerDatosDeTipos(datosDelPokemon)
            movimientos = CargadorDeDatosDePokemons.obtenerDatosDeMovimientos()
            datosEvolucion = CargadorDeDatosDePokemons.obtenerDatosDeEvolucion(nombre)
            

            datosFormateadosDePokemon = dict()
            datosFormateadosDePokemon['indicePokedex'] = indicePokedex
            datosFormateadosDePokemon['nombre'] = nombre
            datosFormateadosDePokemon['estadisticas'] = estadisticas
            datosFormateadosDePokemon['tipos'] = tipos
            datosFormateadosDePokemon['movimientos'] = movimientos
            datosFormateadosDePokemon['evolucion'] = datosEvolucion

            datosFormateadosDePokemons.append(datosFormateadosDePokemon)

        return datosFormateadosDePokemons


    def obtenerDatosDeEstadisticas(datosDelPokemon: dict) -> dict: #se obtienen las estadisticas a partir de un pokemon
        stats = datosDelPokemon['stats']
        nombres = [stat['stat']['name'] for stat in stats]
        valores = [stat['base_stat'] for stat in stats]
        datosFormateadosDeEstadisticas = dict(zip(nombres, valores))
        return datosFormateadosDeEstadisticas


    def obtenerDatosDeMovimientos() -> list: #se obtienen 4 movimientos al azar elegidos de la respuesta de la API directamente
        cantidadDeMovimientos = 4
        rangoDeIdsDeMovimientos = list(range(1, 900))
        idsDeMovimientos = Randomizador.obtenerMuestra(rangoDeIdsDeMovimientos, cantidadDeMovimientos)

        datosDeMovimientos = []
        for id in idsDeMovimientos:
            url = os.path.join(URL_MOVIMIENTOS, str(id))
            datosMovimiento = requests.get(url).json()
            datosDeMovimientos.append(datosMovimiento)


        datosFormateadosDeMovimientos = []
        for datos in datosDeMovimientos:
            nombre = datos['name']
            precision = datos['accuracy'] if datos['accuracy'] else 50
            potencia = datos['power'] if datos['power'] else 50
            tipo = datos['type']['name']

            datosFormateadosDeMovimiento = {'nombre':nombre, 'precision': precision, 'potencia':potencia, 'tipo': tipo}
            datosFormateadosDeMovimientos.append(datosFormateadosDeMovimiento)

        return datosFormateadosDeMovimientos


    def obtenerDatosDeTipos(datosDelPokemon: dict) -> list:
        datosDeTipos = datosDelPokemon['types']
        datosFormateadosDeTipos = [datos['type']['name'] for datos in datosDeTipos]
        return datosFormateadosDeTipos
    

    def obtenerDatosDeEvolucion(nombreDePokemon: str) -> list:
        response = requests.get(os.path.join(URL_ESPECIES_POKEMON, nombreDePokemon))
        datosEspeciePokemon = response.json()
        urlCadenaEvolutiva = datosEspeciePokemon['evolution_chain']['url']

        datosDeEvolucionDeEspecie = requests.get(urlCadenaEvolutiva).json()

        if datosDeEvolucionDeEspecie['chain']['evolves_to']:
            urlEvolucionDeEspecie = datosDeEvolucionDeEspecie['chain']['evolves_to'][0]['species']['url']
        else:
            return None

        datosDeEvolucionDeEspecie = requests.get(urlEvolucionDeEspecie).json()

        idEvolucion = datosDeEvolucionDeEspecie['id']

        return CargadorDeDatosDePokemons.obtenerDatosDePokemonPorId(idEvolucion)



