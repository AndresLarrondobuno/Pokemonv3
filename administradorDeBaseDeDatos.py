import pandas as pd
from generadorDeValoresAlAzar import GeneradorDeValoresAlAzar
from cargadorDeDatos import CargadorDeDatos
from formateadorDeDatos import FormateadorDeDatos
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
        for id in range(1, 10):
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
        for id in range(1, 10):
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
        '''adaptar metodo para que utilice crearTabla, para esto necesito un metodo que facilite formatear la consulta de forma que
        incluya a las referencias y otro que haga lo mismo con las restricciones'''

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




