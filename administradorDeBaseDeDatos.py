import pandas as pd
from generadorDeValoresAlAzar import GeneradorDeValoresAlAzar
from cargadorDeDatos import CargadorDeDatos
from formateadorDeDatos import FormateadorDeDatos
from pokemon import Pokemon
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
        for id in range(1, 250):
            datosMovimiento = CargadorDeDatos.cargarDatosDeMovimiento(id)
            datosDeMovimientoFormateados = FormateadorDeDatos.formatearDatosDeMovimiento(datosMovimiento)
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
        for id in range(1, 152):
            datosPokemon = CargadorDeDatos.cargarDatosDePokemon(id)
            datosPokemonFormateados = FormateadorDeDatos.formatearDatosDePokemon(datosPokemon)
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
        no pude adaptar metodo para que utilice crearTabla, para esto necesito un metodo que facilite formatear la consulta de forma que
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
        movimientosAdquiribles = [CargadorDeDatos.cargarMovimientosAdquiriblesDe(id) for id in range(1, 152)]
        for datos in movimientosAdquiribles:
            for nombreDePokemon, nombresDeMovimientos in datos.items():
                idPokemon = self.obtenerIdDePokemonPorNombre(nombreDePokemon)
                for nombreDeMovimiento in nombresDeMovimientos:
                    idMovimiento = self.obtenerIdDeMovimientoPorNombre(nombreDeMovimiento)
                    #if idPokemon and idMovimiento:
                    self.insertarCombinacionDeIdsATablaMovimientosAdquiribles(idPokemon, idMovimiento)


    def obtenerIdDeMovimientoPorNombre(self, nombre: str):
        consulta = f'''SELECT id FROM movimientos WHERE nombre = '{nombre}'
        '''
        self.ejecutarConsulta(consulta)
        try:
            return self.cursor.fetchone()
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
        consulta = f''' SELECT * FROM movimientos WHERE id IN
        (SELECT movimiento_id FROM movimientos_adquiribles WHERE pokemon_id IN
        (SELECT id FROM pokemons WHERE id='{id}'))
        '''
        self.ejecutarConsulta(consulta)
        return self.cursor.fetchall()
    

    def obtenerEquipoPokemon(self, tamanoDeEquipo: int) -> list[Pokemon]:
        datosPokemons = [self.obtenerDatosDePokemonPorId(id) for id in idsPokemons]
        idsPokemons = [datos[0][0] for datos in datosPokemons]
        datosMovimientos = [self.obtenerDatosDeMovimientosDePokemon(id) for id in idsPokemons]
        datosMovimientos = [GeneradorDeValoresAlAzar.obtenerMuestra(datosMovimientos, 4) for x in range(tamanoDeEquipo)]
        print(datosMovimientos)

        nombre = datosPokemons[1]
        tipos = [datosPokemons[2], datosPokemons[3]]
        movimientos = []
        estadisticas = [datos[0][-1:-6] for datos in datosPokemons]
        pokemon = Pokemon(nombre, tipos, movimientos, estadisticas)
        return


    def obtenerDatosDePokemonPorId(self, id: int) -> tuple:
        consulta = f'''SELECT * FROM pokemons WHERE id = {id}'''
        self.ejecutarConsulta(consulta)
        resultado = self.cursor.fetchall()
        return resultado
    

    def obtenerDatosDeMovimientoPorId(self, id: int) -> tuple:
        consulta = f'''SELECT * FROM movimientos WHERE id = {id}'''
        self.ejecutarConsulta(consulta)
        resultado = self.cursor.fetchall()
        return resultado
    




