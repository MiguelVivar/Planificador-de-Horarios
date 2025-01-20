import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from modules.validador import validar_datos
from modules.excel import guardar_en_excel
from modules.conflictos import verificar_conflicto


# Función para validar datos
def validar_datos(curso, empieza, termina, profesor):
    if not curso or not empieza or not termina or not profesor:
        return "Todos los campos son obligatorios.", False
    if empieza >= termina:
        return "La hora de inicio debe ser menor que la hora de término.", False
    return "Datos validados correctamente.", True

# Función ficticia para verificar conflictos (esto debe definirse en el archivo `guardar_excel.py`)
def verificar_conflicto(hoja, curso, dia, empieza, termina, salon):
    return "No hay conflictos.", True  # Aquí puedes usar la lógica real de conflictos.

def iniciar():
    def on_validar():
        # Obtener valores de los campos
        curso = entrada_curso.get()
        ciclo = ciclo_var.get()
        seccion = seccion_var.get()
        dia = dia_var.get()
        empieza = empieza_var.get()
        termina = termina_var.get()
        salon = salon_var.get()
        tipo = tipo_var.get()
        profesor = entrada_profesor.get()

        # Validar datos
        mensaje, continuar = validar_datos(curso, empieza, termina, profesor)
        if continuar:
            # Guardar datos en Excel
            resultado = guardar_en_excel(
                curso, ciclo, seccion, dia, empieza, termina, salon, tipo, profesor, verificar_conflicto
            )
            if "correctamente" in resultado:
                messagebox.showinfo("Éxito", "El horario fue guardado exitosamente.")
            else:
                messagebox.showerror("Error", resultado)
        else:
            messagebox.showwarning("Advertencia", mensaje)

    def salir():
        if messagebox.askyesno("Salir", "¿Estás seguro de que deseas salir?"):
            root.destroy()

    # Configuración de la ventana principal
    root = tk.Tk()
    root.title("Planificador Moderno")
    root.geometry("700x800")
    root.configure(bg="#2E4053")

    # Estilo
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font=("Arial", 14, "bold"), padding=10, background="#58D68D", foreground="white")
    style.map("TButton", background=[("active", "#45B39D")])
    style.configure("TLabel", background="#2E4053", foreground="white", font=("Arial", 12))
    style.configure("TEntry", font=("Arial", 12), padding=5)
    style.configure("TCombobox", font=("Arial", 12))

    # Encabezado
    header = tk.Label(root, text="Planificador de Horarios", font=("Arial", 24, "bold"), bg="#2E4053", fg="#F4D03F")
    header.pack(pady=20)

    # Contenedor principal
    frame = ttk.Frame(root, padding=20, style="TFrame")
    frame.pack(expand=True, fill="both", padx=20, pady=20)

    # Entradas y menús desplegables
    elementos = [
        ("Curso:", ttk.Entry(frame)),
        ("Ciclo:", ttk.Combobox(frame, values=["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"], state="readonly")),
        ("Sección:", ttk.Combobox(frame, values=["A", "B"], state="readonly")),
        ("Día:", ttk.Combobox(frame, values=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"], state="readonly")),
        ("Hora de inicio:", ttk.Combobox(frame, values=["07:45", "08:30", "09:15", "10:00", "10:45", "11:30", "12:15", "13:00"], state="readonly")),
        ("Hora de término:", ttk.Combobox(frame, values=["08:30", "09:15", "10:00", "10:45", "11:30", "12:15", "13:00", "13:45"], state="readonly")),
        ("Número de salón:", ttk.Combobox(frame, values=[f"A{i:03d}" for i in range(101, 106)], state="readonly")),
        ("Tipo de clase:", ttk.Combobox(frame, values=["Teoría", "Práctica"], state="readonly")),
        ("Profesor:", ttk.Entry(frame)),
    ]

    for i, (label_text, widget) in enumerate(elementos):
        ttk.Label(frame, text=label_text).grid(row=i, column=0, sticky="e", padx=10, pady=10)
        widget.grid(row=i, column=1, sticky="w", padx=10, pady=10)

    # Asignar entradas específicas a variables
    entrada_curso = elementos[0][1]
    ciclo_var = elementos[1][1]
    seccion_var = elementos[2][1]
    dia_var = elementos[3][1]
    empieza_var = elementos[4][1]
    termina_var = elementos[5][1]
    salon_var = elementos[6][1]
    tipo_var = elementos[7][1]
    entrada_profesor = elementos[8][1]

    # Botones
    boton_guardar = ttk.Button(frame, text="Validar y Guardar", command=on_validar)
    boton_guardar.grid(row=len(elementos), column=0, columnspan=2, pady=20)

    boton_salir = ttk.Button(frame, text="Salir", command=salir)
    boton_salir.grid(row=len(elementos) + 1, column=0, columnspan=2, pady=10)

    root.mainloop()