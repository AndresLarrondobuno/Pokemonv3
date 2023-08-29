import pandas as pd
from generadorDeValoresAlAzar import GeneradorDeValoresAlAzar
from cargadorDeDatos import CargadorDeDatos
from formateadorDeDatos import FormateadorDeDatos
from pokemon import Pokemon
from movimiento import Movimiento
import sqlite3
import time


pd.set_option('display.max_colwidth', 800)
class AdministradorDeBaseDeDatos:
    '''
    Almacena datos en una base de datos y puede realizarle consultas SQL (CRUD)
    '''

    def __init__(self, nombre: str): 
        self.conexion = sqlite3.connect(nombre + '.db')
        self.cursor = self.conexion.cursor()
    

    def ejecutarConsulta(self, consulta: str, parametros: list = None):
        if parametros:
            self.cursor.execute(consulta, parametros)
        else:
            self.cursor.execute(consulta)


    def ejecutarConsultaDeCambio(self, consulta: str, parametros: list = None):
        if parametros:
            self.cursor.execute(consulta, parametros)
        else:
            self.cursor.execute(consulta)
        self.conexion.commit()


    def crearTabla(self, nombre: str, nombresDeColumnasConTiposDeDatos: list[str]):

        consulta = f'''
            CREATE TABLE IF NOT EXISTS {nombre}(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            {nombresDeColumnasConTiposDeDatos})
        '''
        self.ejecutarConsulta(consulta)


    def insertarFila(self, nombreDeTabla: str, valores: dict):
        nombresDeColumnasFormateados = [':' + nombreDeColumna for nombreDeColumna in valores.keys()]
        nombresDeColumnasFormateados = ', '.join(nombresDeColumnasFormateados)
        nombresDeColumnasFormateados = 'NULL, ' + nombresDeColumnasFormateados

        consulta = f"INSERT INTO {nombreDeTabla} VALUES ({nombresDeColumnasFormateados})"
        self.ejecutarConsultaDeCambio(consulta, valores)


    def insertarMovimientos(self):
        inicio = time.time()
        for id in range(1, 200):
            datosMovimiento = CargadorDeDatos.cargarDatosDeMovimiento(id)
            datosDeMovimientoFormateados = FormateadorDeDatos.formatearDatosDeMovimientoParaInsercionABaseDeDatos(datosMovimiento)
            tiposDeDatos = ['TEXT', 'INTEGER', 'TEXT', 'INTEGER']
            nombresDeColumnas = datosDeMovimientoFormateados.keys()
            nombresDeColumnasConTiposDeDatos = FormateadorDeDatos.agregarTiposDeDatosAColumnas(nombresDeColumnas, tiposDeDatos)
            self.crearTabla('movimientos', nombresDeColumnasConTiposDeDatos)
            self.insertarFila('movimientos', datosDeMovimientoFormateados)
            print(datosDeMovimientoFormateados['nombre'] + ' agregado a la db.')

        fin = time.time()
        print(f'duracion: {fin-inicio}')


    def insertarPokemons(self):
        inicio = time.time()
        for id in range(1, 50):
            datosPokemon = CargadorDeDatos.cargarDatosDePokemon(id)
            datosPokemonFormateados = FormateadorDeDatos.formatearDatosDePokemonParaInsercionABaseDeDatos(datosPokemon)
            tiposDeDatos = ['TEXT', 'TEXT', 'TEXT', 'INTEGER', 'INTEGER', 'INTEGER', 'INTEGER', 'INTEGER', 'INTEGER']
            nombresDeColumnas = datosPokemonFormateados.keys()
            nombresDeColumnasConTiposDeDatos = FormateadorDeDatos.agregarTiposDeDatosAColumnas(nombresDeColumnas, tiposDeDatos)

            self.crearTabla('pokemons', nombresDeColumnasConTiposDeDatos)
            self.insertarFila('pokemons', datosPokemonFormateados)
            print(datosPokemonFormateados['nombre'] + ' agregado a la db.')

        fin = time.time()
        print(f'duracion: {fin-inicio}')
    

    def crearTablaMovimientosAdquiribles(self):
        '''
        no pude adaptar metodo para que utilice crearTabla, para esto necesito un metodo formatee la consulta de forma que
        incluya a las referencias y otro que haga lo mismo con las restricciones
        '''

        consulta = f'''CREATE TABLE IF NOT EXISTS movimientos_adquiribles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pokemon_id INTEGER,
        movimiento_id INTEGER,
        FOREIGN KEY (pokemon_id) REFERENCES pokemons(id),
        FOREIGN KEY (movimiento_id) REFERENCES  movimientos(id),
        UNIQUE (pokemon_id, movimiento_id) )
        '''
        self.ejecutarConsulta(consulta)


    def insertarCombinacionDeIdsATablaMovimientosAdquiribles(self, idPokemon: int, idMovimiento: int):
        valores = {'idPokemon': idPokemon, 'idMovimiento': idMovimiento}
        self.insertarFila('movimientos_adquiribles', valores)
    

    def insertarFilasAMovimientosAdquiribles(self):
        idsDeseadas = range(1, 50)
        movimientosAdquiribles = [CargadorDeDatos.cargarMovimientosAdquiriblesDe(id) for id in idsDeseadas]
        for datos in movimientosAdquiribles:
            for nombreDePokemon, nombresDeMovimientos in datos.items():
                idPokemon = self.obtenerIdDePokemonPorNombre(nombreDePokemon)
                for nombreDeMovimiento in nombresDeMovimientos:
                    idMovimiento = self.obtenerIdDeMovimientoPorNombre(nombreDeMovimiento)
                    if idPokemon and idMovimiento:
                        self.insertarCombinacionDeIdsATablaMovimientosAdquiribles(idPokemon, idMovimiento)


    def obtenerIdDeMovimientoPorNombre(self, nombre: str):
        consulta = f'''SELECT id FROM movimientos WHERE nombre = '{nombre}'
        '''
        self.ejecutarConsulta(consulta)
        try:
            return self.cursor.fetchone()[0]
        except TypeError:
            return None
    

    def obtenerIdDePokemonPorNombre(self, nombre: str):
        consulta = f'''SELECT id FROM pokemons WHERE nombre = '{nombre}'
        '''
        self.ejecutarConsulta(consulta)
        try:
            return self.cursor.fetchone()[0]
        except TypeError:
            return None
    

    def obtenerDatosDeMovimientosDePokemon(self, id: int):
        consulta = f'''SELECT * FROM movimientos WHERE id IN
        (SELECT movimiento_id FROM movimientos_adquiribles WHERE pokemon_id IN
        (SELECT id FROM pokemons WHERE id='{id}'))
        '''
        self.ejecutarConsulta(consulta)
        return self.cursor.fetchall()
    

    def obtenerEquipoPokemon(self, tamanoDeEquipo: int) -> list[Pokemon]:
        idsTablaPokemon = self.obtenerTodosLosIdsDeTabla('pokemons') #contempla si la db tuvo registros truncados
        idsPokemons = GeneradorDeValoresAlAzar.obtenerMuestra(idsTablaPokemon, tamanoDeEquipo)
        equipo = []

        for id in idsPokemons:
            datosPokemon = self.obtenerDatosDePokemonPorId(id)
            datosMovimientosAdquiribles = self.obtenerDatosDeMovimientosDePokemon(id)
            datosMovimientosElegidosAlAzar = GeneradorDeValoresAlAzar.obtenerMuestra(datosMovimientosAdquiribles, 4)

            movimientos = []
            for datosMovimiento in datosMovimientosElegidosAlAzar:
                movimiento = self.instanciarMovimiento(datosMovimiento)
                movimientos.append(movimiento)
            
            nombre = datosPokemon[1]
            tipos = [datosPokemon[2], datosPokemon[3]]
            estadisticas = {'vida':datosPokemon[4],
                            'ataque':datosPokemon[5],
                            'defensa':datosPokemon[6],
                            'ataque-especial':datosPokemon[7],
                            'defensa-especial':datosPokemon[8],
                            'velocidad':datosPokemon[9]}
            pokemon = Pokemon(nombre, tipos, movimientos, estadisticas)
            equipo.append(pokemon)

        return equipo

    def instanciarMovimiento(self, datosMovimiento: tuple) -> Movimiento:
        '''instancia un movimiento a partir de los datos obtenidos de la DB'''
        if datosMovimiento:
            nombre = datosMovimiento[1]
            potencia = datosMovimiento[2]
            precision = datosMovimiento[3]
            tipo = datosMovimiento[4]
            movimiento = Movimiento(nombre, potencia, precision, tipo)
            return movimiento


    def obtenerDatosDePokemonPorId(self, id: int) -> tuple:
        consulta = f'''SELECT * FROM pokemons WHERE id = {id}'''
        self.ejecutarConsulta(consulta)
        return self.cursor.fetchone()


    def obtenerDatosDeMovimientoPorId(self, id: int) -> tuple:
        consulta = f'''SELECT * FROM movimientos WHERE id = {id}'''
        self.ejecutarConsulta(consulta)
        resultado = self.cursor.fetchall()
        return resultado


    def obtenerCantidadDeRegistrosDeTabla(self, tabla: str):
        consulta = f"SELECT COUNT(*) FROM {tabla}"
        self.ejecutarConsulta(consulta)
        return self.cursor.fetchone()[0]


    def obtenerTodosLosIdsDeTabla(self, tabla: str):
        consulta = f"SELECT id FROM {tabla}"
        self.ejecutarConsulta(consulta)
        resultados = self.cursor.fetchall()
        resultados = [resultado[0] for resultado in resultados]
        #es necesario porque cada fila aunque sea de 1 elemento se obtiene como tupla ej: [(1,), (2,), (3,)] -> [1, 2, 3]
        return resultados