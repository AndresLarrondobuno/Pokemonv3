from AdministradorDeBaseDeDatos import AdministradorDeBaseDeDatos
import requests_cache, requests, os

requests_cache.install_cache('CachePokemonsGeneracionUno')

if __name__ == '__main__':
    administradorDeBaseDeDatos = AdministradorDeBaseDeDatos('pokemon')

    administradorDeBaseDeDatos.insertarPokemons()

    administradorDeBaseDeDatos.insertarMovimientos()

    administradorDeBaseDeDatos.crearTablaMovimientosAdquiribles()

    administradorDeBaseDeDatos.insertarFilasAMovimientosAdquiribles()