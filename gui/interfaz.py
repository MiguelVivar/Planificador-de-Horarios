import tkinter as tk
from tkinter import ttk

# Datos de los profesores y sus cursos
profesores_cursos = {
    "ANGULO QUISPE ALEJANDRO ISAIAS": "LIDERAZGO, FUNDAMENTOS DE MICROECONOMÍa, FINANZAS Y CONTABILIDAD, ORGANIZACIÓN Y ADMINISTRACIÓN DE EMPRESAS",
    "CHAMORRO HUAMANI LORENZO": "MATEMÁTICA SUPERIOR",
    "CHAVEZ GUILLEN ROLANDO": "INTRODUCCIÓN A LA INFORMÁTICA, FUNDAMENTOS DE LENGUAJE DE PROGRAMACIÓN",
    "CORDOVA FARFAN CARLOS": "SISTEMAS DE INFORMACIÓN",
    "GUEVARA GARIBAY HENRY": "SOCIOLOGÍa, DEFENSA NACIONAL Y DESASTRES NATURALES",
    "HUARANCCA CONTRERAS PATRICIA": "ESTADÍSTICA APLICADA, INTELIGENCIA DE NEGOCIOS, INVESTIGACIÓN FORMATIVA",
    "JIMENEZ GRAVITO JUAN": "ARQUITECTURA DE DATA CENTER",
    "LLANCAYA RAMIREZ FLAVIO": "FÍSICA APLICADA A LA INGENIERÍa DE SISTEMAS",
    "MARQUEZ URBINA PACO": "SOLUCIONES MÓVILES Y CLOUD, ADMINISTRACIÓN DE BD",
    "MENDOZA CABALLERO ENRIQUE": "GESTIÓN DEL CONOCIMIENTO",
    "PALOMINO HERRERA MERY HILDA": "MATEMÁTICA SUPERIOR, CÁLCULO DIFERENCIAL APLICADO A LA INGENIERÍa DE SISTEMAS, CÁLCULO INTEGRAL APLICADO A LA INGENIERÍa DE SISTEMAS",
    "PEÑA CASAS EDGAR": "PROYECTO DE TESIS II",
    "PEÑA CASAS ERWIN PABLO": "INTRODUCCIÓN A LA INGENIERÍa DE SISTEMAS, MATEMÁTICA SUPERIOR, FUNDAMENTOS DE ARQUITECTURA EMPRESARIAL",
    "PINEDA MORAN SELENE": "INTRODUCCIÓN A LA FORMACIÓN PROFESIONAL",
    "PUCHURI MANCO YESSICA": "INTERFAZ HOMBRE MÁQUINA",
    "QUISPE ARCOS HANS": "SEGURIDAD Y AUDITORÍa DE SISTEMAS",
    "QUISPE TINCOPA LINO": "INTRODUCCIÓN A LA INFORMÁTICA, ALGORITMO Y ESTRUCTURA DE DATOS",
    "ROMERO LOYOLA HENRY": "CÁLCULO DIFERENCIAL APLICADO A LA INGENIERÍa DE SISTEMAS, SEGURIDAD Y AUDITORÍa DE SISTEMAS",
    "SALCEDO HERNANDEZ MONICA GABRIELA": "INTRODUCCIÓN A LA FORMACIÓN PROFESIONAL",
    "VENTURA FERNANDEZ FREDDY": "INVESTIGACIÓN FORMATIVA, LENGUAJE Y COMUNICACIÓN, REDACCIÓN Y TÉCNICAS DE LA COMUNICACIÓN, PLANIFICACIÓN ESTRATÉGICA DE TI, ÉTICA Y SOCIEDAD",
}

# Crear la ventana principal
root = tk.Tk()
root.title("Profesores y Cursos")

# Etiqueta para el curso
label_curso = tk.Label(root, text="Curso:")
label_curso.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_curso = tk.Entry(root)
entry_curso.grid(row=0, column=1, padx=10, pady=5)

# Etiqueta para el profesor
label_profesor = tk.Label(root, text="Nombre del profesor:")
label_profesor.grid(row=1, column=0, padx=10, pady=5, sticky="e")

# Menú desplegable de profesores
profesor_seleccionado = tk.StringVar()
profesor_desplegable = ttk.Combobox(root, textvariable=profesor_seleccionado)
profesor_desplegable["values"] = list(profesores_cursos.keys())
profesor_desplegable.grid(row=1, column=1, padx=10, pady=5)

# Funcionalidad para mostrar los cursos del profesor seleccionado
def mostrar_cursos():
    profesor = profesor_seleccionado.get()
    cursos = profesores_cursos.get(profesor, "No hay cursos disponibles para este profesor.")
    label_cursos.config(text=f"Cursos: {cursos}")

# Botón para mostrar los cursos
boton_mostrar = tk.Button(root, text="Mostrar Cursos", command=mostrar_cursos)
boton_mostrar.grid(row=2, column=0, columnspan=2, pady=10)

# Etiqueta para mostrar los cursos
label_cursos = tk.Label(root, text="")
label_cursos.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Iniciar la aplicación
root.mainloop()

