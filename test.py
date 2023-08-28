import sqlite3

conexion = sqlite3.connect('pokemons.db')
cursor = conexion.cursor()


datosPokemon = [
{"pikachu": ["trueno", "impactrueno"]},
{"bulbasaur": ["tacle", "latigo-cepa"]}
]


for datos in datosPokemon:
    for x, y in datos.items():
        print(x, y)

lista = [1,2,3,4]
print(lista[1:2])