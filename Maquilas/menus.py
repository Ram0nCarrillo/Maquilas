"""
Interfaz gráfica para el sistema de gestión de maquilas usando Tkinter.
Incluye funcionalidades para manejar áreas, operadores y supervisores.
Cada pestaña permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar).
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from entities.area import Area
from entities.operador import Operador
from entities.supervisor import Supervisor
from persistence.db import SessionLocal

session = SessionLocal()

# ------------------------ FUNCIONES DE CONSULTA ------------------------
def listar_areas():
    return session.query(Area).all()

def listar_operadores():
    return session.query(Operador).all()

def listar_supervisores():
    return session.query(Supervisor).all()

# ------------------------ CLASE PRINCIPAL ------------------------
class App(tk.Tk):
    """Clase principal que contiene la aplicación Tkinter."""
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión de Maquilas")
        self.geometry("1000x700")
        self.config(bg="#f0f0f0")

        # Crear tabs para cada entidad
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)

        self.create_area_tab()
        self.create_operador_tab()
        self.create_supervisor_tab()

    # ------------------------ TAB AREAS ------------------------
    def create_area_tab(self):
        """Crea la pestaña para gestionar las áreas."""
        area_frame = ttk.Frame(self.notebook)
        self.notebook.add(area_frame, text="Áreas")

        self.area_tree = ttk.Treeview(area_frame, columns=("ID", "Departamento", "Descripción"), show='headings')
        for col in self.area_tree["columns"]:
            self.area_tree.heading(col, text=col)
        self.area_tree.pack(fill='both', expand=True)

        ttk.Button(area_frame, text="Actualizar", command=self.load_areas).pack()

        entry_frame = ttk.Frame(area_frame)
        entry_frame.pack(pady=10)

        ttk.Label(entry_frame, text="Departamento").grid(row=0, column=0)
        self.dep_entry = ttk.Entry(entry_frame)
        self.dep_entry.grid(row=0, column=1)

        ttk.Label(entry_frame, text="Descripción").grid(row=1, column=0)
        self.desc_entry = ttk.Entry(entry_frame)
        self.desc_entry.grid(row=1, column=1)

        self.load_areas()

    def load_areas(self):
        """Carga las áreas desde la base de datos y actualiza la tabla."""
        for row in self.area_tree.get_children():
            self.area_tree.delete(row)
        for area in listar_areas():
            self.area_tree.insert('', 'end', values=(area.id, area.departamento, area.descripcion))

    # ------------------------ TAB OPERADORES ------------------------
    def create_operador_tab(self):
        """Crea la pestaña para gestionar operadores."""
        operador_frame = ttk.Frame(self.notebook)
        self.notebook.add(operador_frame, text="Operadores")

        self.operador_tree = ttk.Treeview(
            operador_frame,
            columns=("ID", "Nombre", "Sexo", "Fecha Ingreso", "Turno", "Salario", "Área", "Supervisor"),
            show='headings'
        )
        for col in self.operador_tree["columns"]:
            self.operador_tree.heading(col, text=col)
        self.operador_tree.pack(fill='both', expand=True)
        self.operador_tree.bind("<<TreeviewSelect>>", self.fill_operador_entries)

        ttk.Button(operador_frame, text="Actualizar", command=self.load_operadores).pack()

        entry_frame = ttk.Frame(operador_frame)
        entry_frame.pack(pady=10)

        self.operador_entries = []
        labels = ["Nombre", "Sexo", "Fecha Ingreso (YYYY-MM-DD)", "Turno", "Salario", "Área ID", "Supervisor ID"]
        for idx, label in enumerate(labels):
            ttk.Label(entry_frame, text=label).grid(row=idx, column=0, sticky="e")
            entry = ttk.Entry(entry_frame)
            entry.grid(row=idx, column=1)
            self.operador_entries.append(entry)

        button_row = len(labels)
        ttk.Button(entry_frame, text="Agregar Operador", command=self.add_operador).grid(row=button_row, column=0, pady=5, padx=5)
        ttk.Button(entry_frame, text="Editar Operador", command=self.edit_operador).grid(row=button_row, column=1, pady=5, padx=5)
        ttk.Button(entry_frame, text="Eliminar Operador", command=self.delete_operador).grid(row=button_row, column=2, pady=5, padx=5)

        self.load_operadores()

    def load_operadores(self):
        """Carga los operadores y actualiza la tabla."""
        for row in self.operador_tree.get_children():
            self.operador_tree.delete(row)
        for o in listar_operadores():
            area = o.area.departamento if o.area else "Sin área"
            supervisor = o.supervisor.nombre if o.supervisor else "Sin supervisor"
            self.operador_tree.insert('', 'end', values=(o.id, o.nombre, o.sexo, o.fecha_ingreso, o.turno, o.salario, o.id_area, o.id_supervisor))

    def add_operador(self):
        """Agrega un nuevo operador a la base de datos."""
        try:
            nombre = self.operador_entries[0].get()
            sexo = self.operador_entries[1].get()
            fecha = datetime.strptime(self.operador_entries[2].get(), "%Y-%m-%d").date()
            turno = self.operador_entries[3].get()
            salario = float(self.operador_entries[4].get())
            id_area = int(self.operador_entries[5].get())
            id_supervisor = int(self.operador_entries[6].get())

            nuevo = Operador(
                nombre=nombre, sexo=sexo, fecha_ingreso=fecha,
                turno=turno, salario=salario,
                id_area=id_area, id_supervisor=id_supervisor
            )
            session.add(nuevo)
            session.commit()
            self.load_operadores()
            for entry in self.operador_entries:
                entry.delete(0, 'end')
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def fill_operador_entries(self, event):
        """Rellena los campos del formulario con datos del operador seleccionado."""
        selected = self.operador_tree.selection()
        if selected:
            values = self.operador_tree.item(selected[0])["values"]
            self.selected_operador_id = values[0]
            for i in range(1, len(values)):
                self.operador_entries[i - 1].delete(0, 'end')
                self.operador_entries[i - 1].insert(0, values[i])

    def edit_operador(self):
        """Edita al operador seleccionado."""
        try:
            if not hasattr(self, "selected_operador_id"):
                messagebox.showinfo("Seleccionar", "Selecciona un operador primero")
                return

            operador = session.query(Operador).filter_by(id=self.selected_operador_id).first()
            if operador:
                operador.nombre = self.operador_entries[0].get()
                operador.sexo = self.operador_entries[1].get()
                operador.fecha_ingreso = datetime.strptime(self.operador_entries[2].get(), "%Y-%m-%d").date()
                operador.turno = self.operador_entries[3].get()
                operador.salario = float(self.operador_entries[4].get())
                operador.id_area = int(self.operador_entries[5].get())
                operador.id_supervisor = int(self.operador_entries[6].get())

                session.commit()
                self.load_operadores()
                messagebox.showinfo("Éxito", "Operador actualizado correctamente")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_operador(self):
        """Elimina el operador seleccionado."""
        selected = self.operador_tree.focus()
        if not selected:
            messagebox.showinfo("Seleccionar", "Selecciona un operador a eliminar")
            return
        item = self.operador_tree.item(selected)
        operador_id = item['values'][0]
        operador = session.query(Operador).filter_by(id=operador_id).first()
        if operador:
            session.delete(operador)
            session.commit()
            self.load_operadores()

    # ------------------------ TAB SUPERVISORES ------------------------
    def create_supervisor_tab(self):
        """Crea la pestaña para gestionar supervisores."""
        supervisor_frame = ttk.Frame(self.notebook)
        self.notebook.add(supervisor_frame, text="Supervisores")

        self.supervisor_tree = ttk.Treeview(
            supervisor_frame,
            columns=("ID", "Nombre", "Sexo", "Fecha de ingreso (YYYY-MM-DD)", "Turno", "Salario", "Teléfono", "Correo", "ID Área"),
            show='headings'
        )
        for col in self.supervisor_tree["columns"]:
            self.supervisor_tree.heading(col, text=col)
        self.supervisor_tree.pack(fill='both', expand=True)

        self.supervisor_tree.bind("<<TreeviewSelect>>", self.fill_supervisor_entries)
        ttk.Button(supervisor_frame, text="Actualizar", command=self.load_supervisores).pack()

        entry_frame = ttk.Frame(supervisor_frame)
        entry_frame.pack(pady=10)

        self.supervisor_entries = []
        labels = ["Nombre", "Sexo", "Fecha de ingreso (YYYY-MM-DD)", "Turno", "Salario", "Teléfono", "Correo", "ID Área"]
        for idx, label_text in enumerate(labels):
            ttk.Label(entry_frame, text=label_text).grid(row=idx, column=0, sticky="e")
            entry = ttk.Entry(entry_frame)
            entry.grid(row=idx, column=1)
            self.supervisor_entries.append(entry)

        ttk.Button(entry_frame, text="Editar Supervisor", command=self.edit_supervisor).grid(row=len(labels), columnspan=2, pady=5)

        self.load_supervisores()

    def load_supervisores(self):
        """Carga los supervisores en la tabla."""
        for row in self.supervisor_tree.get_children():
            self.supervisor_tree.delete(row)
        for s in listar_supervisores():
            self.supervisor_tree.insert('', 'end', values=(
                s.id, s.nombre, s.sexo, s.fecha_ingreso, s.turno,
                s.salario, s.telefono, s.correo, s.id_area
            ))

    def fill_supervisor_entries(self, event):
        """Rellena los campos del formulario con datos del supervisor seleccionado."""
        selected = self.supervisor_tree.selection()
        if selected:
            values = self.supervisor_tree.item(selected[0])["values"]
            self.selected_supervisor_id = values[0]
            for i in range(1, len(values)):
                self.supervisor_entries[i - 1].delete(0, 'end')
                self.supervisor_entries[i - 1].insert(0, values[i])

    def edit_supervisor(self):
        """Edita al supervisor seleccionado."""
        try:
            if not hasattr(self, "selected_supervisor_id"):
                messagebox.showinfo("Seleccionar", "Selecciona un supervisor primero")
                return

            supervisor = session.query(Supervisor).filter_by(id=self.selected_supervisor_id).first()
            if supervisor:
                supervisor.nombre = self.supervisor_entries[0].get()
                supervisor.sexo = self.supervisor_entries[1].get()
                supervisor.fecha_ingreso = datetime.strptime(self.supervisor_entries[2].get(), "%Y-%m-%d").date()
                supervisor.turno = self.supervisor_entries[3].get()
                supervisor.salario = float(self.supervisor_entries[4].get())
                supervisor.telefono = self.supervisor_entries[5].get()
                supervisor.correo = self.supervisor_entries[6].get()
                supervisor.id_area = int(self.supervisor_entries[7].get())

                session.commit()
                self.load_supervisores()
                messagebox.showinfo("Éxito", "Supervisor actualizado correctamente")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# ------------------------ EJECUCIÓN ------------------------
if __name__ == "__main__":
    app = App()
    app.mainloop()