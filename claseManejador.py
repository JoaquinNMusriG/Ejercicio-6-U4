class ManejadorProvincias:
    __provincias=None

    def __init__(self):
        self.__provincias=[]

    def agregarProvincia(self, provincia):
        self.__provincias.append(provincia)

    def getListaProvincia(self):
        return self.__provincias

    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                provincias=[provincias.toJSON() for provincias in self.__provincias]
                )
        return d
