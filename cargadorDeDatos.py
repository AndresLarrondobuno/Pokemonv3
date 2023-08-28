import sys
from generadorDeValoresAlAzar import GeneradorDeValoresAlAzar
from formateadorDeDatos import FormateadorDeDatos
import requests

sys.stdout.reconfigure(encoding='utf-8')

URL_POKEMONS = f"https://pokeapi.co/api/v2/pokemon/"
URL_ESPECIES_POKEMON = 'https://pokeapi.co/api/v2/pokemon-species/'
URL_CADENA_EVOLUTIVA = 'https://pokeapi.co/api/v2/evolution-chain/'
URL_TIPOS = f"https://pokeapi.co/api/v2/type/"
URL_MOVIMIENTOS = f"https://pokeapi.co/api/v2/move/"
URL_ESTADISTICAS = f"https://pokeapi.co/api/v2/stat/"


class CargadorDeDatos:
    '''
    Trae desde pokeAPI la informacion de los pokemons en formato JSON
    '''

    def cargarDatosDePokemon(metodoDeIdentificacion: int|str) -> dict:
        url = FormateadorDeDatos.formatearUrl(URL_POKEMONS, metodoDeIdentificacion)
        respuesta = requests.get(url)
        return respuesta.json()


    def cargarDatosDeEspecie(metodoDeIdentificacion: int|str) -> dict:
        url = FormateadorDeDatos.formatearUrl(URL_ESPECIES_POKEMON, metodoDeIdentificacion)
        respuesta = requests.get(url)
        return respuesta.json()


    def cargarDatosDeCadenaEvolutiva(metodoDeIdentificacion: int|str) -> dict:
        url = FormateadorDeDatos.formatearUrl(URL_CADENA_EVOLUTIVA, metodoDeIdentificacion)
        respuesta = requests.get(url)
        return respuesta.json()


    def cargarDatosDeTipo(metodoDeIdentificacion: int|str) -> dict:
        url = FormateadorDeDatos.formatearUrl(URL_TIPOS, metodoDeIdentificacion)
        respuesta = requests.get(url)
        return respuesta.json()


    def cargarDatosDeMovimiento(metodoDeIdentificacion: int|str) -> dict:
        url = FormateadorDeDatos.formatearUrl(URL_MOVIMIENTOS, metodoDeIdentificacion)
        respuesta = requests.get(url)
        return respuesta.json()


    def cargarDatosDeEstadistica(metodoDeIdentificacion: int|str) -> dict:
        url = FormateadorDeDatos.formatearUrl(URL_ESTADISTICAS, metodoDeIdentificacion)
        respuesta = requests.get(url)
        return respuesta.json()


    def cargarMovimientosAdquiriblesDe(idPokemon: int) -> dict:
        url = FormateadorDeDatos.formatearUrl(URL_POKEMONS, idPokemon)
        respuesta = requests.get(url)

        datosPokemon = respuesta.json()
        datosMovimientos = datosPokemon['moves']
        nombreDePokemon = datosPokemon['name']
        movimientosAdquiribles = {nombreDePokemon:[]}

        for datosMovimiento in datosMovimientos:
            url = datosMovimiento['move']['url']
            datosMovimiento = requests.get(url).json()
            esPrevioAGeneracionCuatro = datosMovimiento['generation']['name'] in ['generation-i' or 'generation-ii' or 'generation-iii']
            if esPrevioAGeneracionCuatro:
                nombreDeMovimiento = datosMovimiento['name']
                movimientosAdquiribles[nombreDePokemon].append(nombreDeMovimiento)
                #print(f'movimiento: {nombreDeMovimiento}')
            else:
                nombreDeMovimiento = datosMovimiento['name']
                #print(f'movimiento: {nombreDeMovimiento} -> movimiento de generacion IV en adelante')

        return movimientosAdquiribles


    def a(datosPokemon: dict):
        pass


# # # # # # # # # # # #
    def obtenerIdsDeEvoluciones(nombreDePokemon: str) -> list[int]|None:
        datosDeEspeciePokemon = CargadorDeDatos.cargarDatosDeCadenaEvolutiva(nombreDePokemon)

        urlCadenaEvolutiva = datosDeEspeciePokemon['evolution_chain']['url']
        datosDeCadenaEvolutiva = requests.get(urlCadenaEvolutiva).json()
        cadenaEvolutiva = datosDeCadenaEvolutiva['chain']
        eslabones = CargadorDeDatos.obtenerEslabonesDeCadenaEvolutiva(cadenaEvolutiva)
        posicionDeEspecieEnCadenaEvolutiva = CargadorDeDatos.obtenerPosicionEnCadenaEvolutiva(eslabones, nombreDePokemon)
        eslabon = eslabones[posicionDeEspecieEnCadenaEvolutiva]
        

        esElUltimoEslabon = eslabon == eslabones[-1]

        if esElUltimoEslabon:
            print(f'{nombreDePokemon} no tiene evolucion')
            return None
        else:
            evoluciones = eslabon[0]['evolves_to']
            nombresDeEvoluciones = [evoluciones[i]['species']['name'] for i, evolucion in enumerate(evoluciones)]
            print(f'{nombreDePokemon} evoluciona a: {nombresDeEvoluciones}')
        

        idsDeEvoluciones = []
        for evolucion in evoluciones:
            urlEvolucionDeEspecie = evolucion['species']['url']
            responseEvolucionDeEspecie = requests.get(urlEvolucionDeEspecie)
            datosDeEvolucionDeEspecie = responseEvolucionDeEspecie.json()
            idDeEvolucion = datosDeEvolucionDeEspecie['id']
            idsDeEvoluciones.append(idDeEvolucion)
        return idsDeEvoluciones
    

    def obtenerEslabonesDeCadenaEvolutiva(cadenaEvolutiva: dict) -> list[list[dict]]:
        especiesEnCadenaEvolutiva = [cadenaEvolutiva]
        siguienteEslabon = CargadorDeDatos.obtenerSiguienteEslabon(especiesEnCadenaEvolutiva)
        eslabones = [especiesEnCadenaEvolutiva]

        while siguienteEslabon:
            eslabones.append(siguienteEslabon)
            siguienteEslabon = CargadorDeDatos.obtenerSiguienteEslabon(siguienteEslabon)

        return eslabones
    

    def obtenerPrimerEslabon(cadenaEvolutiva: dict):
        pass


    def obtenerSiguienteEslabon(eslabon: list) -> list|None:
        eslabonActualEsMultiple = len(eslabon) > 1
        for especie in eslabon:
            especieTieneEvolucion = not especie['evolves_to']

        siguienteEslabonEsMultiple = None if esUltimoEslabon else len(eslabon['evolves_to']) > 1

        if esUltimoEslabon:
            siguienteEslabon = None
        else:
            if siguienteEslabonEsMultiple:
                siguienteEslabon = eslabon['evolves_to'] # -> list|None
            else:
                siguienteEslabon = eslabon['evolves_to'][0] # -> dict[list]

        return siguienteEslabon


    def obtenerPosicionEnCadenaEvolutiva(eslabones: list[dict], nombreDePokemon: str) -> int|None:
        pass




