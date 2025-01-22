import tkinter as tk
from tkinter import messagebox
from modules.validador import validar_datos
from modules.excel import guardar_en_excel
from modules.conflictos import verificar_conflicto

def iniciar():
    # Crear la ventana principal de la interfaz
    def on_validar():
        # Obtener datos de entrada desde la interfaz
        curso = entry_curso.get()
        ciclo = ciclo_var.get()
        seccion = seccion_var.get()
        dia = dia_var.get()
        turno = turno_var.get()
        empieza = empieza_var.get()
        termina = termina_var.get()
        salon = salon_var.get()
        tipo = tipo_var.get()
        profesor = entry_profesor.get()

        # Llamar a la función de validación y obtener el mensaje de error o éxito
        mensaje, CONTINUAR = validar_datos(curso, profesor)

        if CONTINUAR:
            # Si es válido, guardamos el horario
            resultado = guardar_en_excel(curso, ciclo, seccion, dia, empieza, termina, salon, tipo, profesor, verificar_conflicto)

            if "Conflicto" in resultado:  # Si el resultado contiene un conflicto
                # Mostrar mensaje de conflicto en rojo en la interfaz
                label_mensaje.config(text="¡Conflicto detectado! " + resultado, fg="red")
            elif "Error" in resultado:  # Si el resultado contiene un mensaje de error
                # Mostrar mensaje de error en rojo
                label_mensaje.config(text=resultado, fg="red")
            else:
                # Actualizar el mensaje de éxito en la interfaz (verde)
                label_mensaje.config(text="Curso agregado correctamente", fg="green")
        else:
            # Si hay conflicto, mostrar el mensaje de error en rojo
            label_mensaje.config(text=mensaje, fg="red")

    def actualizar_horas(*args):
        turno_horas = {
            "Mañana": ["07:45", "08:30", "09:15", "10:00", "10:45", "11:30", "12:15", "13:00", "13:45"],
            "Tarde": ["16:00", "16:45", "17:30", "18:15", "19:00", "19:45", "20:30", "21:15", "22:00"]
        }
        turno = "Mañana" if ciclo_var.get() in ["I", "II", "III", "IV"] else "Tarde"
        horas_inicio = turno_horas[turno]
        horas_termina = turno_horas[turno]

        empieza_var.set(horas_inicio[0])
        termina_var.set(horas_termina[8])

        empieza_menu["menu"].delete(0, "end")
        termina_menu["menu"].delete(0, "end")

        for hora in horas_inicio:
            empieza_menu["menu"].add_command(label=hora, command=tk._setit(empieza_var, hora))
        for hora in horas_termina:
            termina_menu["menu"].add_command(label=hora, command=tk._setit(termina_var, hora))
    
    def actualizar_turno(*args):
        turnos_por_ciclo = {
            "Mañana": ["I", "II", "III", "IV"],  # Ciclos asignados a turno mañana
            "Tarde": ["V", "VI", "VII", "VIII", "IX", "X"]  # Ciclos asignados a turno tarde
        }

        # Determinar el turno según el ciclo seleccionado
        ciclo_actual = ciclo_var.get()
        turno = "Mañana" if ciclo_actual in turnos_por_ciclo["Mañana"] else "Tarde"

        turno_var.set(turno)  # Actualizar el valor del menú de Turno

        # Actualizar las opciones del menú desplegable de Turno
        turno_menu["menu"].delete(0, "end")  # Limpiar las opciones del menú

        for opcion in turnos_por_ciclo:
            turno_menu["menu"].add_command(label=opcion, command=tk._setit(turno_var, opcion))

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Planificador")
    root.state("zoomed")
    root.config(bg="#f0f0f0")  # Color de fondo de la ventana

    # Fuente para los textos
    fuente = ("Arial", 12)

    # Crear y ubicar los widgets (labels, entradas, botones) con mejor alineación
    frame = tk.Frame(root, bg="#f0f0f0", padx=30, pady=30)  # Frame para centralizar los widgets
    frame.pack(expand=True)  # Empaquetamos el frame para que ocupe el 100% de la ventana

    # Crear los labels y entradas de manera centrada
    label_curso = tk.Label(frame, text="Curso:", font=fuente, bg="#f0f0f0")
    label_curso.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_curso = tk.Entry(frame, font=fuente)
    entry_curso.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    # Menú desplegable para Ciclo con números romanos
    label_ciclo = tk.Label(frame, text="Ciclo:", font=fuente, bg="#f0f0f0")
    label_ciclo.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    ciclos_romanos = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    ciclo_var = tk.StringVar(value=ciclos_romanos[0])  # Valor por defecto
    ciclo_var.trace("w", actualizar_horas)  # Llamar a actualizar_horas cuando cambie el ciclo
    ciclo_var.trace("w", actualizar_turno)  # Llamar a actualizar_horas cuando cambie el ciclo
    ciclo_menu = tk.OptionMenu(frame, ciclo_var, *ciclos_romanos)
    ciclo_menu.config(width=15, font=("Arial", 12), bg="#E0E0E0", relief="raised")
    ciclo_menu.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Menú desplegable para Sección
    label_seccion = tk.Label(frame, text="Sección:", font=fuente, bg="#f0f0f0")
    label_seccion.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    secciones = ["A", "B"]  # Opciones de sección
    seccion_var = tk.StringVar(value=secciones[0])  # Valor por defecto
    seccion_menu = tk.OptionMenu(frame, seccion_var, *secciones)
    seccion_menu.config(width=10, font=("Arial", 12), bg="#E0E0E0", relief="raised")
    seccion_menu.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    # Menú desplegable para Día
    label_dia = tk.Label(frame, text="Día:", font=fuente, bg="#f0f0f0")
    label_dia.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    dia_var = tk.StringVar(value=dias[0])  # Valor por defecto
    dia_menu = tk.OptionMenu(frame, dia_var, *dias)
    dia_menu.config(width=15, font=("Arial", 12), bg="#E0E0E0", relief="raised")
    dia_menu.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    # Mostrar turno fijo como etiqueta
    label_turno = tk.Label(frame, text="Turno:", font=fuente, bg="#f0f0f0")
    label_turno.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    turno_var = tk.StringVar(value="Mañana")  # Define el turno fijo como "Mañana"
    turno_label = tk.Label(frame, textvariable=turno_var, font=("Arial", 12), bg="#E0E0E0", relief="raised", width=15)
    turno_label.grid(row=4, column=1, padx=10, pady=10, sticky="w")


    # Menú desplegable para Hora de Inicio
    label_inicio = tk.Label(frame, text="Hora de inicio:", font=fuente, bg="#f0f0f0")
    label_inicio.grid(row=5, column=0, padx=10, pady=10, sticky="w")
    empieza_var = tk.StringVar()
    empieza_menu = tk.OptionMenu(frame, empieza_var, "")
    empieza_menu.config(width=10, font=("Arial", 12), bg="#E0E0E0", relief="raised")
    empieza_menu.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    # Menú desplegable para Hora de Término
    label_termina = tk.Label(frame, text="Hora de término:", font=fuente, bg="#f0f0f0")
    label_termina.grid(row=6, column=0, padx=10, pady=10, sticky="w")
    termina_var = tk.StringVar()
    termina_menu = tk.OptionMenu(frame, termina_var, "")
    termina_menu.config(width=10, font=("Arial", 12), bg="#E0E0E0", relief="raised")
    termina_menu.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    # Menú desplegable para Salón
    label_salon = tk.Label(frame, text="Número de salón:", font=fuente, bg="#f0f0f0")
    label_salon.grid(row=7, column=0, padx=10, pady=10, sticky="w")
    salones = [f"A{i:03d}" for i in range(101, 106)]  # Opciones de salón del A101 al A105
    salon_var = tk.StringVar(value=salones[0])  # Valor por defecto
    salon_menu = tk.OptionMenu(frame, salon_var, *salones)
    salon_menu.config(width=10, font=("Arial", 12), bg="#E0E0E0", relief="raised")
    salon_menu.grid(row=7, column=1, padx=10, pady=10, sticky="w")

    # Menú desplegable para Tipo de clase
    label_tipo = tk.Label(frame, text="Tipo de clase (Teoría o Práctica):", font=fuente, bg="#f0f0f0")
    label_tipo.grid(row=8, column=0, padx=10, pady=10, sticky="w")
    tipos = ["Teoría", "Práctica"]  # Opciones de tipo de clase
    tipo_var = tk.StringVar(value=tipos[0])  # Valor por defecto
    tipo_menu = tk.OptionMenu(frame, tipo_var, *tipos)
    tipo_menu.config(width=15, font=("Arial", 12), bg="#E0E0E0", relief="raised")
    tipo_menu.grid(row=8, column=1, padx=10, pady=10, sticky="w")

    label_profesor = tk.Label(frame, text="Nombre del profesor:", font=fuente, bg="#f0f0f0")
    label_profesor.grid(row=9, column=0, padx=10, pady=10, sticky="w")
    entry_profesor = tk.Entry(frame, font=fuente)
    entry_profesor.grid(row=9, column=1, padx=10, pady=10, sticky="w")

    # Label para mostrar el mensaje de éxito o error
    label_mensaje = tk.Label(frame, text="", font=("Arial", 12, "bold"), fg="red", bg="#f0f0f0")
    label_mensaje.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

    # Botón para validar y guardar el curso
    boton_validar = tk.Button(frame, text="Validar y Guardar", command=on_validar, font=fuente, bg="#4CAF50", fg="white", relief="raised")
    boton_validar.grid(row=11, column=0, columnspan=2, padx=10, pady=20)

    # Ejecutar la interfaz
    root.mainloop()
