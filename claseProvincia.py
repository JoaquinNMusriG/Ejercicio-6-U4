import requests

class Provincia:
    __Nombre = None
    __Capital = None
    __CantHabitantes = None
    __CantDptoPatidos = None
    __Info = None

    def __init__(self, nombre, capital, habitantes, dptopartidos):
        self.__Nombre = nombre
        self.__Capital = self.verificarCapital(capital)
        try:
            self.__CantHabitantes = int(habitantes)
        except ValueError:
            raise ValueError('Cantidad habitantes inválida')
        try:
            self.__CantDptoPatidos = int(dptopartidos)
        except ValueError:
            raise ValueError('Peso inválido')

    def verificarCapital (self, capital):
        complete_url = 'http://api.openweathermap.org/data/2.5/weather?q={},AR&units=metric&appid={}'.format(capital, '9f4fbe968a6c0667c83d62969f9ab117') #ESTA ES MI API KEY
        r = requests.get(complete_url)
        x = r.json()
        if 'main' in x:
            self.__Info = x
            return capital
        raise ValueError('Capital Inválida')

    def getNombre(self):
        return self.__Nombre

    def getCapital(self):
        return self.__Capital

    def getCantHabitantes(self):
        return self.__CantHabitantes

    def getCantDptoPatidos(self):
        return self.__CantDptoPatidos

    def getTemperatura(self):
        return self.__Info['main']['temp']

    def getSencTermica(self):
        return self.__Info['main']['feels_like']
        
    def getHumedad(self):
        return self.__Info['main']['humidity']

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
