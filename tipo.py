


class Tipo:

    MAPA_DE_RELACION_DE_EFECTIVIDAD_ENTRE_TIPOS = {
        'normal': {
            'muy efectivo': [],
            'poco efectivo': ['roca', 'acero'],
            'sin efecto': ['fantasma']
        },
        'lucha': {
            'muy efectivo': ['normal', 'roca', 'acero', 'hielo', 'oscuridad'],
            'poco efectivo': ['volador', 'veneno', 'bicho', 'psiquico', 'hada'],
            'sin efecto': ['fantasma']
        },
        'volador': {
            'muy efectivo': ['lucha', 'bicho', 'planta'],
            'poco efectivo': ['roca', 'acero', 'electrico'],
            'sin efecto': []
        },
        'veneno': {
            'muy efectivo': ['planta', 'hada'],
            'poco efectivo': ['veneno', 'tierra', 'roca', 'fantasma'],
            'sin efecto': ['acero']
        },
        'tierra': {
            'muy efectivo': ['veneno', 'roca', 'acero', 'fuego', 'electrico'],
            'poco efectivo': ['planta'],
            'sin efecto': ['volador']
        },
        'roca': {
            'muy efectivo': ['volador', 'bicho', 'fuego', 'hielo'],
            'poco efectivo': ['lucha', 'tierra', 'acero'],
            'sin efecto': []
        },
        'bicho': {
            'muy efectivo': ['planta', 'psiquico', 'oscuridad'],
            'poco efectivo': [],
            'sin efecto': []
        },
        'fantasma': {
            'muy efectivo': ['fantasma', 'psiquico'],
            'poco efectivo': ['oscuridad', 'acero'],
            'sin efecto': ['normal']
        },
        'acero': {
            'muy efectivo': ['hielo', 'roca', 'hada'],
            'poco efectivo': ['fuego', 'agua', 'electrico', 'acero'],
            'sin efecto': []
        },
        'fuego': {
            'muy efectivo': ['bicho', 'acero', 'planta', 'hielo'],
            'poco efectivo': ['roca', 'fuego', 'agua', 'dragon'],
            'sin efecto': []
        },
        'agua': {
            'muy efectivo': ['tierra', 'roca', 'fuego'],
            'poco efectivo': ['agua', 'planta', 'electrico'],
            'sin efecto': []
        },
        'planta': {
            'muy efectivo': ['tierra', 'roca', 'agua'],
            'poco efectivo': ['volador', 'veneno', 'bicho', 'acero', 'fuego', 'planta', 'dragon'],
            'sin efecto': []
        },
        'electrico': {
            'muy efectivo': ['volador', 'agua'],
            'poco efectivo': ['planta', 'electrico', 'dragon'],
            'sin efecto': ['tierra']
        },
        'psiquico': {
            'muy efectivo': ['lucha', 'veneno'],
            'poco efectivo': ['acero', 'psiquico'],
            'sin efecto': []
        },
        'hielo': {
            'muy efectivo': ['volador', 'tierra', 'planta', 'dragon'],
            'poco efectivo': ['acero', 'fuego', 'agua', 'hielo'],
            'sin efecto': []
        },
        'dragon': {
            'muy efectivo': ['dragon'],
            'poco efectivo': ['acero'],
            'sin efecto': ['hada']
        },
        'oscuridad': {
            'muy efectivo': ['psiquico', 'fantasma'],
            'poco efectivo': ['lucha', 'oscuridad', 'hada'],
            'sin efecto': []
        },
        'hada': {
            'muy efectivo': ['lucha', 'dragon', 'oscuridad'],
            'poco efectivo': ['acero', 'fuego', 'veneno'],
            'sin efecto': ['veneno', 'acero']
        }
    }

    def __init__(self, nombre: str):
        self._nombre = nombre


    def calcularEfectividadContra(self, tipoAtacado) -> 'Tipo':
        mapa = Tipo.MAPA_DE_RELACION_DE_EFECTIVIDAD_ENTRE_TIPOS
        datosDeTipoAtacado: dict = mapa[tipoAtacado]

        for tipo, relacionesDeEfectividad in datosDeTipoAtacado:
            if self.nombre in relacionesDeEfectividad:
                return tipo


if __name__ == "__main__":
    fuego = Tipo('fuego')
    agua = Tipo('agua')

    efectividad = agua.calcularEfectividadContra(fuego)
    print(efectividad)