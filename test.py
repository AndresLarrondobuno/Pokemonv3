import sqlite3

conexion = sqlite3.connect('pokemons.db')
cursor = conexion.cursor()


diccionarioDatosPokemon = {"pikachu": {"nombre":"pikachu", 'tipo':'electrico'}, 
                           "bulbasaur": {"nombre":"bulbasaur", 'tipo':'planta'}
                           }


nombresDeColumnasPokemons = diccionarioDatosPokemon.keys()

nombresDeColumnas = ['nombre', 'tipo', 'ataque', 'defensa']
tiposDeDatos = ['TEXT', 'TEXT', 'INTEGER', 'INTEGER']
camposParaConsulta = zip(nombresDeColumnas, tiposDeDatos)

camposParaConsultaFormateados = []
for nombre, tipoDeDato in camposParaConsulta:
    campo = f'{nombre} {tipoDeDato}'
    camposParaConsultaFormateados.append(campo)

camposParaConsultaFormateados = ', '.join(camposParaConsultaFormateados)

print(camposParaConsultaFormateados)

