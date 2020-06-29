class Provincia:
    __Nombre = None
    __Capital = None
    __CantHabitantes = None
    __CantDptoPatidos = None

    def __init__(self, nombre, capital, habitantes, dptopartidos):
        self.__Nombre = nombre
        self.__Capital = capital
        try:
            self.__CantHabitantes = int(habitantes)
        except ValueError:
            raise ValueError('Cantidad habitantes inválida')
        try:
            self.__CantDptoPatidos = int(dptopartidos)
        except ValueError:
            raise ValueError('Peso inválido')

    def getNombre(self):
        return self.__Nombre

    def getCapital(self):
        return self.__Capital

    def getCantHabitantes(self):
        return self.__CantHabitantes

    def getCantDptoPatidos(self):
        return self.__CantDptoPatidos

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                        nombre = self.__Nombre,
                        capital = self.__Capital,
                        habitantes = self.__CantHabitantes,
                        dptopartidos = self.__CantDptoPatidos
                    )
            )
        return d
