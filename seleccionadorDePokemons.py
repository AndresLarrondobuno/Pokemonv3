from BaseDeDatos.AdministradorDeBaseDeDatos import AdministradorDeBaseDeDatos
from GeneradorDeValoresAlAzar import GeneradorDeValoresAlAzar
from Pokemon import Pokemon
from Movimiento import Movimiento


class SeleccionadorDePokemons:
    '''
    1)Construye las intancias de pokemons en base a la informacion que AdministradorDeBD obtiene de la base de datos
    2)Forma los equipos para los participantes de la batalla
    '''
    def __init__(self, administradorDeBaseDeDatos = AdministradorDeBaseDeDatos('pokemon')):
        self.administradorDeBaseDeDatos = administradorDeBaseDeDatos


    def obtenerEquipoPokemon(self, tamanoDeEquipo: int) -> list[Pokemon]:
        idsTablaPokemon = self.administradorDeBaseDeDatos.obtenerTodosLosIdsDeTabla('pokemons') #contempla si la db tuvo registros truncados
        idsPokemons = GeneradorDeValoresAlAzar.obtenerMuestra(idsTablaPokemon, tamanoDeEquipo)
        equipo = []

        for id in idsPokemons:
            pokemon = self.obtenerPokemon(id)
            equipo.append(pokemon)

        return equipo


    def obtenerPokemon(self, id: int) -> Pokemon:

        datosPokemon = self.administradorDeBaseDeDatos.obtenerDatosDePokemonPorId(id)
        datosMovimientosAdquiribles = self.administradorDeBaseDeDatos.obtenerDatosDeMovimientosDePokemon(id)
        datosMovimientosElegidosAlAzar = GeneradorDeValoresAlAzar.obtenerMuestra(datosMovimientosAdquiribles, 4)

        movimientos = []
        for datosMovimiento in datosMovimientosElegidosAlAzar:
            movimiento = self.obtenerMovimiento(datosMovimiento)
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

        return pokemon
    

    def obtenerMovimiento(self, datosMovimiento: tuple) -> Movimiento:
        '''instancia un movimiento a partir de los datos obtenidos de la DB'''
        if datosMovimiento:
            nombre = datosMovimiento[1]
            potencia = datosMovimiento[2]
            precision = datosMovimiento[3]
            tipo = datosMovimiento[4]
            movimiento = Movimiento(nombre, potencia, precision, tipo)
            return movimiento


''' def obtenerMovimientos(datosMovimientos):
        movimientos = []
        cantidadDeMovimientos = 4
        for indice in range(cantidadDeMovimientos):
            nombre = datosMovimientos[indice]['nombre']
            tipo = datosMovimientos[indice]['tipo']
            potencia = datosMovimientos[indice]['potencia']
            precision = datosMovimientos[indice]['precision']
            movimiento = Movimiento(nombre, tipo, potencia, precision)
            movimientos.append(movimiento)
        return movimientos'''