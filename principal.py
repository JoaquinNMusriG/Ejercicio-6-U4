from claseRepositorio import Respositorio
from claseVista import Aplicacion
from claseControlador import ControladorProvincias
from claseObjectEncoder import ObjectEncoder

if __name__ == "__main__":
    jsonF = ObjectEncoder('datos.json')
    repositorio = Respositorio(jsonF)
    vista = Aplicacion()
    controlador = ControladorProvincias(repositorio, vista)
    vista.setControlador(controlador)
    controlador.start()
    controlador.salirGrabarDatos()
