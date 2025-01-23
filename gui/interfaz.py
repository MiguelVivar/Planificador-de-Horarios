import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from ttkthemes import ThemedTk  # Importar ThemedTk para un tema visual mejorado
from modules.excel import obtener_ciclos, obtener_cursos, obtener_profesores, obtener_salones, guardar_horario_excel
import os
import shutil
import subprocess  # Para abrir el directorio

class VentanaAplicacion:
    def __init__(self, master):
        """
        Inicializa la ventana principal de la aplicación.
        :param master: Ventana raíz de Tkinter.
        """
        self.master = master
        self.master.title("HorariUN")  # Título de la ventana
        self.master.set_theme("equilux")  # Tema oscuro con tonos morados

        # Configurar el fondo morado
        self.master.configure(background="#4B0082")  # Fondo morado

        # Variables de control para los widgets
        self.ciclo_var = tk.StringVar()  # Variable para el ciclo seleccionado
        self.seccion_var = tk.StringVar()  # Variable para la sección seleccionada
        self.curso_var = tk.StringVar()  # Variable para el curso seleccionado
        self.profesor_var = tk.StringVar()  # Variable para el profesor seleccionado
        self.turno_var = tk.StringVar()  # Variable para el turno seleccionado
        self.hora_inicio_var = tk.StringVar()  # Variable para la hora de inicio
        self.hora_fin_var = tk.StringVar()  # Variable para la hora de fin
        self.tipo_clase_var = tk.StringVar()  # Variable para el tipo de clase (Teoría/Práctica)
        self.dia_clase_var = tk.StringVar()  # Variable para el día de la clase

        # Configurar estilos personalizados para los widgets
        self.setup_styles()

        # Configurar los widgets de la interfaz
        self.setup_widgets()

    def setup_styles(self):
        """
        Configura estilos personalizados para los widgets de la interfaz.
        """
        style = ttk.Style()
        # Estilo para las etiquetas (fondo gris, fuente blanca)
        style.configure("TLabel", font=("Courier", 14), padding=5, foreground="#FFFFFF", background="#2E2E2E")
        # Estilo para los botones (fondo morado, fuente blanca)
        style.configure("TButton", font=("Courier", 14), padding=5, foreground="#FFFFFF", background="#800080")
        style.map("TButton", background=[("active", "#4B0082")])  # Hover: morado más oscuro
        # Estilo para los combobox (fondo blanco, fuente blanca y más grande)
        style.configure("TCombobox", font=("Courier", 12), padding=5, foreground="#FFFFFF", background="#FFFFFF")
        style.map("TCombobox", fieldbackground=[("readonly", "#FFFFFF")], background=[("readonly", "#FFFFFF")])
        # Estilo para el título
        style.configure("Title.TLabel", font=("Courier", 20, "bold"), foreground="#FFFFFF", background="#4B0082")
        # Estilo para el subtítulo
        style.configure("Subtitle.TLabel", font=("Courier", 16), foreground="#FFFFFF", background="#4B0082")
        # Estilo para el frame principal (fondo gris)
        style.configure("Main.TFrame", background="#2E2E2E")

    def setup_widgets(self):
        """
        Configura y organiza los widgets en la ventana principal.
        """
        # Título "Facultad de Ingeniería de Sistemas"
        title_label = ttk.Label(self.master, text="Facultad de Ingeniería de Sistemas", style="Title.TLabel")
        title_label.pack(pady=10)

        # Subtítulo "III Ciclo A"
        subtitle_label = ttk.Label(self.master, text="III Ciclo A", style="Subtitle.TLabel")
        subtitle_label.pack(pady=5)

        # Frame principal para organizar los widgets (fondo gris)
        main_frame = ttk.Frame(self.master, padding="20", style="Main.TFrame")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")  # Centrar el frame en la ventana

        # Widgets dentro del bloque gris
        ttk.Label(main_frame, text="Selecciona el Ciclo:").grid(row=0, column=0, pady=5, padx=5, sticky="w")
        self.ciclo_menu = ttk.Combobox(main_frame, textvariable=self.ciclo_var, state="readonly")
        self.ciclo_menu.grid(row=0, column=1, pady=5, padx=5, sticky="ew")

        ttk.Label(main_frame, text="Selecciona el Turno:").grid(row=1, column=0, pady=5, padx=5, sticky="w")
        self.turno_menu = ttk.Entry(main_frame, textvariable=self.turno_var, state="readonly")
        self.turno_menu.grid(row=1, column=1, pady=5, padx=5, sticky="ew")

        ttk.Label(main_frame, text="Selecciona la Sección:").grid(row=2, column=0, pady=5, padx=5, sticky="w")
        self.seccion_menu = ttk.Combobox(main_frame, textvariable=self.seccion_var, state="readonly")
        self.seccion_menu.grid(row=2, column=1, pady=5, padx=5, sticky="ew")

        ttk.Label(main_frame, text="Selecciona el Curso:").grid(row=3, column=0, pady=5, padx=5, sticky="w")
        self.curso_menu = ttk.Combobox(main_frame, textvariable=self.curso_var, state="readonly")
        self.curso_menu.grid(row=3, column=1, pady=5, padx=5, sticky="ew")

        ttk.Label(main_frame, text="Selecciona el Profesor:").grid(row=4, column=0, pady=5, padx=5, sticky="w")
        self.profesor_menu = ttk.Combobox(main_frame, textvariable=self.profesor_var, state="readonly")
        self.profesor_menu.grid(row=4, column=1, pady=5, padx=5, sticky="ew")

        ttk.Label(main_frame, text="Hora de Inicio:").grid(row=5, column=0, pady=5, padx=5, sticky="w")
        self.hora_inicio_menu = ttk.Combobox(main_frame, textvariable=self.hora_inicio_var, state="readonly")
        self.hora_inicio_menu.grid(row=5, column=1, pady=5, padx=5, sticky="ew")

        ttk.Label(main_frame, text="Hora de Fin:").grid(row=6, column=0, pady=5, padx=5, sticky="w")
        self.hora_fin_menu = ttk.Combobox(main_frame, textvariable=self.hora_fin_var, state="readonly")
        self.hora_fin_menu.grid(row=6, column=1, pady=5, padx=5, sticky="ew")

        ttk.Label(main_frame, text="Tipo de Clase:").grid(row=7, column=0, pady=5, padx=5, sticky="w")
        self.tipo_clase_menu = ttk.Combobox(main_frame, textvariable=self.tipo_clase_var, state="readonly", values=["Teoría", "Práctica"])
        self.tipo_clase_menu.grid(row=7, column=1, pady=5, padx=5, sticky="ew")

        ttk.Label(main_frame, text="Selecciona el Día de la Clase:").grid(row=8, column=0, pady=5, padx=5, sticky="w")
        self.dia_clase_menu = ttk.Combobox(main_frame, textvariable=self.dia_clase_var, state="readonly", values=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"])
        self.dia_clase_menu.grid(row=8, column=1, pady=5, padx=5, sticky="ew")

        ttk.Label(main_frame, text="Selecciona el Salón:").grid(row=9, column=0, pady=5, padx=5, sticky="w")
        self.salon_menu = ttk.Combobox(main_frame, state="readonly")
        self.salon_menu.grid(row=9, column=1, pady=5, padx=5, sticky="ew")

        # Funciones de actualización
        self.ciclo_var.trace("w", self.actualizar_datos)
        self.ciclo_var.trace("w", self.actualizar_cursos)
        self.curso_var.trace("w", self.actualizar_profesores)

        # Botones
        button_frame = ttk.Frame(main_frame, style="Main.TFrame")
        button_frame.grid(row=10, column=0, columnspan=2, pady=10)

        ttk.Button(button_frame, text="Cargar datos", command=self.cargar_archivo).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Generar Horario", command=self.generar_horario).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Ver Horarios", command=self.ver_horarios).grid(row=0, column=2, padx=5)

    def cargar_archivo(self):
        """
        Abre un cuadro de diálogo para seleccionar un archivo Excel y lo copia a la carpeta 'data'.
        """
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
        """
        Actualiza los ciclos disponibles en el combobox correspondiente.
        """
        try:
            ciclos = obtener_ciclos()
            self.ciclo_menu["values"] = [c[0] for c in ciclos]
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer los ciclos: {e}")

    def actualizar_salones(self):
        """
        Actualiza los salones disponibles en el combobox correspondiente.
        """
        try:
            salones = obtener_salones()
            self.salon_menu["values"] = salones
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer los salones: {e}")

    def actualizar_datos(self, *args):
        """
        Actualiza las secciones y el turno según el ciclo seleccionado.
        """
        ciclo_seleccionado = self.ciclo_var.get()
        for ciclo, secciones, turno in obtener_ciclos():
            if ciclo == ciclo_seleccionado:
                self.seccion_menu["values"] = secciones.split(",")
                self.turno_var.set(turno)
                self.actualizar_horas(turno)
                break

    def actualizar_cursos(self, *args):
        """
        Actualiza los cursos disponibles según el ciclo seleccionado.
        """
        ciclo_seleccionado = self.ciclo_var.get()
        cursos = obtener_cursos(ciclo_seleccionado)
        self.curso_menu["values"] = cursos

    def actualizar_profesores(self, *args):
        """
        Actualiza los profesores disponibles según el curso seleccionado.
        """
        curso_seleccionado = self.curso_var.get()
        profesores = obtener_profesores(curso_seleccionado)
        self.profesor_menu["values"] = profesores

    def actualizar_horas(self, turno):
        """
        Actualiza las horas de inicio y fin según el turno seleccionado.
        :param turno: Turno seleccionado (Mañana/Tarde).
        """
        horas_inicio, horas_fin = self.generar_horas(turno)
        self.hora_inicio_menu["values"] = horas_inicio
        self.hora_fin_menu["values"] = horas_fin

    def generar_horas(self, turno):
        """
        Genera las horas de inicio y fin según el turno.
        :param turno: Turno seleccionado (Mañana/Tarde).
        :return: Listas de horas de inicio y fin.
        """
        if turno == "Mañana":
            horas_inicio = ["07:45", "08:30", "09:15", "10:00", "10:45", "11:30", "12:15", "13:00"]
            horas_fin = ["08:30", "09:15", "10:00", "10:45", "11:30", "12:15", "13:00", "13:45"]
        else:
            horas_inicio = ["16:00", "16:45", "17:30", "18:15", "19:00", "19:45", "20:30", "21:15"]
            horas_fin = ["16:45", "17:30", "18:15", "19:00", "19:45", "20:30", "21:15", "22:00"]

        return horas_inicio, horas_fin

    def generar_horario(self):
        """
        Genera un horario y lo guarda en un archivo Excel.
        """
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
        """
        Abre la carpeta donde se guardan los horarios generados.
        """
        directorio_horarios = os.path.join("data", "horarios")
        if os.path.exists(directorio_horarios):
            subprocess.Popen(f'explorer "{directorio_horarios}"')
        else:
            messagebox.showwarning("Aviso", "No se han generado horarios aún.")

def iniciar():
    """
    Inicia la aplicación y muestra la ventana principal.
    """
    root = ThemedTk(theme="equilux")  # Usar ThemedTk para un tema visual moderno
    app = VentanaAplicacion(root)
    root.protocol("WM_DELETE_WINDOW", root.quit)  # Salir al cerrar la ventana
    root.state("zoomed")  # Maximizar la ventana
    root.mainloop()