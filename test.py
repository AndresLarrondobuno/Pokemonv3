
def sumarUno(numero: int) -> int:
    return numero + 1


def sumarDos(numero: int) -> int:
    return numero + 2


diccionario = {'sumarUno':sumarUno(1), 'sumarDos': sumarDos(1)}

print(diccionario['sumarUno'])

'''
cuando se crean las jugadas puedo compararlas para decidir:
*el orden en que se ejecutan (chequeo de velocidad)
*la legalidad en el contexto en que se ejecutan
*estas tareas pueden ser asignadas a objeto Arbitro
    i)administrar el conteo de turnos
    ii)chequeo de legalidad
    iii)orden de ejecucion
'''