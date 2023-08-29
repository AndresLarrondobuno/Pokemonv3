import os

class FormateadorDeDatos:

    @staticmethod
    def formatearDatosDePokemonParaInsercionABaseDeDatos(datosPokemon: dict) -> dict:
        datosFormateados = dict()
        datosDeTiposFormateados = FormateadorDeDatos.formatearDatosDeTipos(datosPokemon['types'])
        datosDeEstadisticasFormateados = FormateadorDeDatos.formatearDatosDeEstadisticasParaInsercionABaseDeDatos(datosPokemon['stats'])

        datosFormateados['nombre'] = datosPokemon['name']
        datosFormateados['tipoPrincipal'] = datosDeTiposFormateados['tipoPrincipal']
        datosFormateados['tipoSecundario'] = datosDeTiposFormateados['tipoSecundario']
        datosFormateados['vida'] = datosDeEstadisticasFormateados['vida']
        datosFormateados['ataque'] = datosDeEstadisticasFormateados['ataque']
        datosFormateados['defensa'] = datosDeEstadisticasFormateados['defensa']
        datosFormateados['ataqueEspecial'] = datosDeEstadisticasFormateados['ataqueEspecial']
        datosFormateados['defensaEspecial'] = datosDeEstadisticasFormateados['defensaEspecial']
        datosFormateados['velocidad'] = datosDeEstadisticasFormateados['velocidad']
        return datosFormateados

    
    @staticmethod
    def formatearDatosDeMovimientoParaInsercionABaseDeDatos(datosMovimiento: dict) -> dict:
        datosFormateados = dict()
        datosFormateados['nombre'] = datosMovimiento['name']
        datosFormateados['potencia'] = datosMovimiento['power']
        datosFormateados['precision'] = datosMovimiento['accuracy']
        datosFormateados['tipo'] = datosMovimiento['type']['name']

        return datosFormateados
    

    @staticmethod
    def formatearDatosDeEstadisticasParaInsercionABaseDeDatos(datosEstadisticas: list) -> dict:
        datosFormateados = dict()
        datosFormateados['vida'] = datosEstadisticas[0]['base_stat']
        datosFormateados['ataque'] = datosEstadisticas[1]['base_stat']
        datosFormateados['defensa'] = datosEstadisticas[2]['base_stat']
        datosFormateados['ataqueEspecial'] = datosEstadisticas[3]['base_stat']
        datosFormateados['defensaEspecial'] = datosEstadisticas[4]['base_stat']
        datosFormateados['velocidad'] = datosEstadisticas[5]['base_stat']
        return datosFormateados
    

    @staticmethod
    def formatearDatosDeTipos(datosTipos: list) -> dict:
        datosFormateados = dict()
        datosFormateados['tipoPrincipal'] = datosTipos[0]['type']['name']
        if len(datosTipos) == 2:
            datosFormateados['tipoSecundario'] = datosTipos[1]['type']['name']
        else:
            datosFormateados['tipoSecundario'] = None
        return datosFormateados


    @staticmethod
    def formatearUrlParaConsumirRecursoDeAPI(url: str, metodoDeIdentificacion: int|str) -> str:
        if isinstance(metodoDeIdentificacion, int):
            url = os.path.join(url, str(metodoDeIdentificacion))
        elif isinstance(metodoDeIdentificacion, str):
            url = os.path.join(url, metodoDeIdentificacion)
        else:
            raise ValueError("El argumento debe ser un ID numérico o un nombre de movimiento")
        return url


    @staticmethod
    def agregarTiposDeDatosAColumnas(nombresDeColumnas: list, tiposDeDatos: list) -> str:
        #que se agreguen los items en el teambuilder
        camposParaConsulta = zip(nombresDeColumnas, tiposDeDatos)

        camposParaConsultaFormateados = []
        for nombre, tipoDeDato in camposParaConsulta:
            campo = f'{nombre} {tipoDeDato}'
            camposParaConsultaFormateados.append(campo)

        camposParaConsultaFormateados = ', '.join(camposParaConsultaFormateados)
        return camposParaConsultaFormateados


    '''
    @staticmethod
    def homogeneizarTiposDeDatosDeEslabones(eslabones: list[dict,list]|list[dict]) -> list[list]:
        eslabonesHomogeneizados = []
        for eslabon in eslabones:
            if type(eslabon) == dict:
                eslabon = [eslabon]
            eslabonesHomogeneizados.append(eslabon)
        return eslabonesHomogeneizados
    '''


