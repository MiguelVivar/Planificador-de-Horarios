import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from modules.excel import obtener_ciclos, obtener_cursos, obtener_profesores, obtener_salones, guardar_horario_excel
from datetime import datetime
import os
import shutil
import subprocess  # Para abrir el directorio

class VentanaAplicacion:
    def __init__(self, master):
        self.master = master
        self.master.title("Planificador de Horarios")
        
        # Variables de control
        self.ciclo_var = tk.StringVar()
        self.seccion_var = tk.StringVar()
        self.curso_var = tk.StringVar()
        self.profesor_var = tk.StringVar()
        self.turno_var = tk.StringVar()
        self.hora_inicio_var = tk.StringVar()
        self.hora_fin_var = tk.StringVar()
        self.tipo_clase_var = tk.StringVar()
        self.dia_clase_var = tk.StringVar()  # Nueva variable para el día de la clase

        # Widgets
        self.setup_widgets()

    def setup_widgets(self):
        ttk.Label(self.master, text="Selecciona el Ciclo:").grid(row=0, column=0, pady=5, padx=5, sticky="w")
        self.ciclo_menu = ttk.Combobox(self.master, textvariable=self.ciclo_var, state="readonly")
        self.ciclo_menu.grid(row=0, column=1, pady=5, padx=5)

        ttk.Label(self.master, text="Selecciona el Turno:").grid(row=1, column=0, pady=5, padx=5, sticky="w")
        self.turno_menu = ttk.Entry(self.master, textvariable=self.turno_var, state="readonly")
        self.turno_menu.grid(row=1, column=1, pady=5, padx=5)

        ttk.Label(self.master, text="Selecciona la Sección:").grid(row=2, column=0, pady=5, padx=5, sticky="w")
        self.seccion_menu = ttk.Combobox(self.master, textvariable=self.seccion_var, state="readonly")
        self.seccion_menu.grid(row=2, column=1, pady=5, padx=5)

        ttk.Label(self.master, text="Selecciona el Curso:").grid(row=3, column=0, pady=5, padx=5, sticky="w")
        self.curso_menu = ttk.Combobox(self.master, textvariable=self.curso_var, state="readonly")
        self.curso_menu.grid(row=3, column=1, pady=5, padx=5)

        ttk.Label(self.master, text="Selecciona el Profesor:").grid(row=4, column=0, pady=5, padx=5, sticky="w")
        self.profesor_menu = ttk.Combobox(self.master, textvariable=self.profesor_var, state="readonly")
        self.profesor_menu.grid(row=4, column=1, pady=5, padx=5)

        ttk.Label(self.master, text="Hora de Inicio:").grid(row=5, column=0, pady=5, padx=5, sticky="w")
        self.hora_inicio_menu = ttk.Combobox(self.master, textvariable=self.hora_inicio_var, state="readonly")
        self.hora_inicio_menu.grid(row=5, column=1, pady=5, padx=5)

        ttk.Label(self.master, text="Hora de Fin:").grid(row=6, column=0, pady=5, padx=5, sticky="w")
        self.hora_fin_menu = ttk.Combobox(self.master, textvariable=self.hora_fin_var, state="readonly")
        self.hora_fin_menu.grid(row=6, column=1, pady=5, padx=5)

        # Menú desplegable para Tipo de Clase
        ttk.Label(self.master, text="Tipo de Clase:").grid(row=7, column=0, pady=5, padx=5, sticky="w")
        self.tipo_clase_menu = ttk.Combobox(self.master, textvariable=self.tipo_clase_var, state="readonly", values=["Teoría", "Práctica"])
        self.tipo_clase_menu.grid(row=7, column=1, pady=5, padx=5)

        # Menú desplegable para seleccionar el día de la clase
        ttk.Label(self.master, text="Selecciona el Día de la Clase:").grid(row=8, column=0, pady=5, padx=5, sticky="w")
        self.dia_clase_menu = ttk.Combobox(self.master, textvariable=self.dia_clase_var, state="readonly", values=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"])
        self.dia_clase_menu.grid(row=8, column=1, pady=5, padx=5)

        # Menú despelgable para seleccionar el salón
        ttk.Label(self.master, text="Selecciona el Salón:").grid(row=9, column=0, pady=5, padx=5, sticky="w")
        self.salon_menu = ttk.Combobox(self.master, state="readonly")
        self.salon_menu.grid(row=9, column=1, pady=5, padx=5)
        self.actualizar_salones()

        # Funciones de actualización
        self.ciclo_var.trace("w", self.actualizar_datos)
        self.ciclo_var.trace("w", self.actualizar_cursos)
        self.curso_var.trace("w", self.actualizar_profesores)

        # Botones
        ttk.Button(self.master, text="Cargar datos", command=self.cargar_archivo).grid(row=10, column=0, pady=5, padx=5)
        ttk.Button(self.master, text="Generar Horario", command=self.generar_horario).grid(row=10, column=1, pady=5, padx=5)
        ttk.Button(self.master, text="Ver Horarios", command=self.ver_horarios).grid(row=10, column=2, pady=5, padx=5)

    def cargar_archivo(self):
        archivo_seleccionado = filedialog.askopenfilename(title="Selecciona el archivo que contenga los datos", filetypes=[("Archivos Excel", "*.xlsx")])

        if archivo_seleccionado:
            ruta_destino = "data/datos.xlsx"
            try:
                if not os.path.exists(ruta_destino):
                    os.makedirs("data", exist_ok=True)
                shutil.copy(archivo_seleccionado, ruta_destino)
                messagebox.showinfo("Éxito", "Archivo cargado correctamente.")
                self.actualizar_ciclos()
                self.actualizar_salones()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
        else:
            messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")

    def actualizar_ciclos(self):
        try:
            ciclos = obtener_ciclos()
            self.ciclo_menu["values"] = [c[0] for c in ciclos]
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer los ciclos: {e}")

    def actualizar_datos(self, *args):
        ciclo_seleccionado = self.ciclo_var.get()
        for ciclo, secciones, turno in obtener_ciclos():
            if ciclo == ciclo_seleccionado:
                self.seccion_menu["values"] = secciones.split(",")
                self.turno_var.set(turno)
                self.actualizar_horas(turno)
                break

    def actualizar_cursos(self, *args):
        ciclo_seleccionado = self.ciclo_var.get()
        cursos = obtener_cursos(ciclo_seleccionado)
        self.curso_menu["values"] = cursos

    def actualizar_profesores(self, *args):
        curso_seleccionado = self.curso_var.get()
        profesores = obtener_profesores(curso_seleccionado)
        self.profesor_menu["values"] = profesores

    def actualizar_horas(self, turno):
        horas_inicio, horas_fin = self.generar_horas(turno)
        self.hora_inicio_menu["values"] = horas_inicio
        self.hora_fin_menu["values"] = horas_fin

    def actualizar_salones(self):
        salones = obtener_salones()
        self.salon_menu["values"] = salones

    def generar_horas(self, turno):
        if turno == "Mañana":
            horas_inicio = ["07:45", "08:30", "09:15", "10:00", "10:45", "11:30", "12:15", "13:00"]
            horas_fin = ["08:30", "09:15", "10:00", "10:45", "11:30", "12:15", "13:00", "13:45"]
        else:
            horas_inicio = ["16:00", "16:45", "17:30", "18:15", "19:00", "19:45", "20:30", "21:15"]
            horas_fin = ["16:45", "17:30", "18:15", "19:00", "19:45", "20:30", "21:15", "22:00"]

        return horas_inicio, horas_fin

    def generar_horario(self):
        ciclo = self.ciclo_var.get()
        seccion = self.seccion_var.get()
        curso = self.curso_var.get()
        profesor = self.profesor_var.get()
        hora_inicio = self.hora_inicio_var.get()
        hora_fin = self.hora_fin_var.get()
        tipo_clase = self.tipo_clase_var.get()
        dia_clase = self.dia_clase_var.get()
        salon = self.salon_menu.get()
        turno = self.turno_var.get()

        if not all([ciclo, seccion, curso, profesor, hora_inicio, hora_fin, tipo_clase, dia_clase, salon, turno]):
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return

        # Guardar el horario generado en un archivo Excel
        resultado = guardar_horario_excel(ciclo, seccion, hora_inicio, hora_fin, curso, profesor, tipo_clase, dia_clase, salon, turno)
        if "correctamente" in resultado:
                messagebox.showinfo("Éxito", f"Horario generado para el ciclo {ciclo}, sección {seccion}.")
        else:
            messagebox.showerror("Error", resultado)

    def ver_horarios(self):
        directorio_horarios = os.path.join("data", "horarios")
        if os.path.exists(directorio_horarios):
            subprocess.Popen(f'explorer "{directorio_horarios}"')
        else:
            messagebox.showwarning("Aviso", "No se han generado horarios aún.")

def iniciar():
    root = tk.Tk()
    app = VentanaAplicacion(root)
    root.protocol("WM_DELETE_WINDOW", root.quit)  # Para evitar que se reinicie cuando se cierra la ventana
    root.state("zoomed")  # Maximizar la ventana
    root.mainloop()

# Ejecutar la función iniciar para iniciar la interfaz
if __name__ == "__main__":
    iniciar()