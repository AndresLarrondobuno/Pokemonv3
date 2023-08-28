


class Tipo:

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