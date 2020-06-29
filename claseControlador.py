from claseVista import nuevaProvincia
from claseManejador import ManejadorProvincias

class ControladorProvincias:
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.provincias = list(repo.obtenerListaProvincia())

    def crearProvincia(self):
        nProvincia = nuevaProvincia(self.vista).show()
        if nProvincia:
            provincia = self.repo.agregarUnaProvincia(nProvincia)
            self.provincias.append(provincia)
            self.vista.agregarProvincia(provincia)

    def seleccionarProvincia(self, index):
        self.seleccion = index
        provincia = self.provincias[index]
        self.vista.verProvinciaEnForm(provincia)

    def start(self):
        for c in self.provincias:
            self.vista.agregarProvincia(c)
        self.vista.mainloop()

    def salirGrabarDatos(self):
        self.repo.grabarDatos()
