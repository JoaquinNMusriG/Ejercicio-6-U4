from claseManejador import ManejadorProvincias

class Respositorio:
    __jsonF=None
    __manejador=None

    def __init__(self, jsonF):
        self.__jsonF = jsonF
        try:
            diccionario = self.__jsonF.leerJSONArchivo()
            self.__manejador = self.__jsonF.decodificarDiccionario(diccionario)
        except FileNotFoundError:
            self.__manejador = ManejadorProvincias()

    def obtenerListaProvincia(self):
        return self.__manejador.getListaProvincia()

    def agregarUnaProvincia(self, provincia):
        self.__manejador.agregarProvincia(provincia)
        return provincia

    def grabarDatos(self):
        self.__jsonF.guardarJSONArchivo(self.__manejador.toJSON())
