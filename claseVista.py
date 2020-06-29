import tkinter as tk
from tkinter import messagebox
from claseProvincia import Provincia

class ListaBoxProvincias(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.listab = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.listab.yview)
        self.listab.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.listab.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar(self, provincia, index=tk.END):
        text = "{}".format(provincia.getNombre())
        self.listab.insert(index, text)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.listab.curselection()[0])
        self.listab.bind("<Double-Button-1>", handler)

class FormularioProvincias(tk.LabelFrame):
    def __init__(self, master, fields):
        super().__init__(master, text="Provincia", padx=10, pady=10)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(fields)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    def mostrarEstadoProvinciaEnFormulario(self, provincia):
        values = (provincia.getNombre(), provincia.getCapital(), provincia.getCantHabitantes(), provincia.getCantDptoPatidos())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def crearProvinciaDesdeFormulario(self):
        values = [e.get() for e in self.entries]
        provincia=None
        try:
            provincia = Provincia(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return provincia

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

class nuevaProvincia(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Nueva Provincia')
        self.unaProvincia = None
        self.form = FormularioProvincias(self, ('Nombre','Capital','Cantidad de Habitantes','Cantidad de Departamentos/Partidos'))
        self.btn_confirmar = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_confirmar.pack(pady=10)

    def confirmar(self):
        self.unaProvincia = self.form.crearProvinciaDesdeFormulario()
        if self.unaProvincia:
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.unaProvincia

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Provincias")
        self.listB = ListaBoxProvincias(self, height=15)
        self.form = FormularioProvincias(self, ('Nombre','Capital','Cantidad de Habitantes','Cantidad de Departamentos/Partidos','Temperatura','Sensacion Térmica','Humedad'))
        self.btn_new = tk.Button(self, text="Agregar Provincia")
        self.listB.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)

    def setControlador(self, ctrl):
        self.btn_new.config(command=ctrl.crearProvincia)
        self.listB.bind_doble_click(ctrl.seleccionarProvincia)

    def agregarProvincia(self, provincia):
        self.listB.insertar(provincia)

    def obtenerCambios(self):
        return self.form.crearProvinciaDesdeFormulario()

    def verProvinciaEnForm(self, provincia):
        self.form.mostrarEstadoProvinciaEnFormulario(provincia)
