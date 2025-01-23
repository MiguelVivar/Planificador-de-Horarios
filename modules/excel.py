import pandas as pd
import os
import openpyxl
from openpyxl.styles import PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datetime import datetime, timedelta

def aplicar_bordes_y_relleno(cell, color_fondo):
    """
    Aplica bordes y relleno de color a una celda de Excel.
    :param cell: Celda a la que se aplicarán los estilos.
    :param color_fondo: Color de fondo de la celda.
    """
    color_borde = "000000"  # Color del borde (negro)
    cell.alignment = Alignment(horizontal="center", vertical="center")
    cell.border = Border(
        left=Side(border_style="thin", color=color_borde),
        right=Side(border_style="thin", color=color_borde),
        top=Side(border_style="thin", color=color_borde),
        bottom=Side(border_style="thin", color=color_borde)
    )
    cell.fill = PatternFill(start_color=color_fondo, end_color=color_fondo, fill_type="solid")

def obtener_ciclos():
    """
    Obtiene los ciclos disponibles desde el archivo Excel.
    :return: Lista de tuplas con (ciclo, secciones, turno).
    """
    try:
        df = pd.read_excel("data/datos.xlsx", sheet_name="Ciclos")
        return [(str(row[0]), row[1], row[2]) for row in df.itertuples(index=False, name=None)]
    except Exception as e:
        print(f"Error al leer la hoja 'Ciclos': {e}")
        return []

def obtener_cursos(ciclo):
    """
    Obtiene los cursos disponibles para un ciclo específico.
    :param ciclo: Ciclo seleccionado.
    :return: Lista de cursos.
    """
    try:
        df = pd.read_excel("data/datos.xlsx", sheet_name="Cursos")
        cursos = df[df['Ciclo'] == ciclo]['Curso'].tolist()
        return cursos
    except Exception as e:
        print(f"Error al leer la hoja 'Cursos': {e}")
        return []

def obtener_profesores(curso):
    """
    Obtiene los profesores disponibles para un curso específico.
    :param curso: Curso seleccionado.
    :return: Lista de profesores.
    """
    try:
        df = pd.read_excel("data/datos.xlsx", sheet_name="Profesores")
        profesores = df[df['Cursos'].str.contains(curso)]['Profesor'].tolist()
        return profesores
    except Exception as e:
        print(f"Error al leer la hoja 'Profesores': {e}")
        return []
    
def obtener_salones():
    """
    Obtiene los salones disponibles desde el archivo Excel.
    :return: Lista de salones.
    """
    try:
        df = pd.read_excel("data/datos.xlsx", sheet_name="Salones")
        salones = df['Salón'].tolist()
        return salones
    except Exception as e:
        print(f"Error al leer la hoja 'Salones': {e}")
        return []

def guardar_horario_excel(ciclo, seccion, empieza, termina, curso, profesor, tipo, dia, salon, turno):
    """
    Guarda el horario generado en un archivo Excel.
    :param ciclo: Ciclo seleccionado.
    :param seccion: Sección seleccionada.
    :param empieza: Hora de inicio de la clase.
    :param termina: Hora de fin de la clase.
    :param curso: Curso seleccionado.
    :param profesor: Profesor seleccionado.
    :param tipo: Tipo de clase (Teoría/Práctica).
    :param dia: Día de la clase.
    :param salon: Salón seleccionado.
    :param turno: Turno seleccionado (Mañana/Tarde).
    :return: Mensaje de éxito o error.
    """
    nombre_archivo = f"horario_{ciclo}_{seccion}.xlsx"
    ruta_carpeta = "data/horarios"
    
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
    
    archivo_excel = os.path.join(ruta_carpeta, nombre_archivo)
    
    try:
        wb = openpyxl.load_workbook(archivo_excel)
        hoja = wb.active
    except FileNotFoundError:
        wb = openpyxl.Workbook()
        hoja = wb.active
        hoja.append(["Hora", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])

    color_encabezado = "ADD8E6"  # Color de fondo para el encabezado
    color_fila_par = "F0F8FF"    # Color de fondo para filas pares
    color_fila_impar = "FFFFFF"  # Color de fondo para filas impares
    color_borde = "000000"       # Color del borde

    if turno == "Mañana":
        horas = [
            ("07:45", "08:30"),
            ("08:30", "09:15"),
            ("09:15", "10:00"),
            ("10:00", "10:45"),
            ("10:45", "11:30"),
            ("11:30", "12:15"),
            ("12:15", "01:00"),
            ("01:00", "01:45")
        ]
    else:
        horas = [
            ("16:00", "16:45"),
            ("16:45", "17:30"),
            ("17:30", "18:15"),
            ("18:15", "19:00"),
            ("19:00", "19:45"),
            ("19:45", "20:30"),
            ("20:30", "21:15"),
            ("21:15", "22:00")
        ]

    for i, (hora_inicio, hora_fin) in enumerate(horas):
        hora_cell = hoja.cell(row=i + 2, column=1, value=f"{hora_inicio} - {hora_fin}")
        hora_cell.alignment = Alignment(horizontal="center", vertical="center")
        hora_cell.border = Border(
            left=Side(border_style="thin", color=color_borde),
            right=Side(border_style="thin", color=color_borde),
            top=Side(border_style="thin", color=color_borde),
            bottom=Side(border_style="thin", color=color_borde)
        )

    for col in range(1, 9):
        encabezado_cell = hoja.cell(row=1, column=col)
        encabezado_cell.fill = PatternFill(start_color=color_encabezado, end_color=color_encabezado, fill_type="solid")
        aplicar_bordes_y_relleno(encabezado_cell, color_encabezado)
    
    hora_inicio = datetime.strptime(empieza, "%H:%M")
    hora_termina = datetime.strptime(termina, "%H:%M")
    fila_inicio = (hora_inicio - datetime(2000, 1, 1, 7, 45)).seconds // 2700

    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    columna_dia = dias.index(dia) + 2
    
    for i in range(2, len(horas) + 2):
        for j in range(2, 9):
            cell = hoja.cell(row=i, column=j)
            if cell.value is None:
                cell.value = ""
                aplicar_bordes_y_relleno(cell, color_fila_par if i % 2 == 0 else color_fila_impar)

    for i in range(fila_inicio, len(horas)):
        if hora_inicio < hora_termina:
            cell = hoja.cell(row=i + 2, column=columna_dia)
            if cell.value:
                return f"Conflicto: Ya existe un curso en {dia} de {hora_inicio.strftime('%H:%M')} a {termina}"
            
            cell.value = f"{curso} ({salon}) - {tipo}"
            aplicar_bordes_y_relleno(cell, color_fila_par if i % 2 == 0 else color_fila_impar)
            hora_inicio += timedelta(minutes=45)
        else:
            break

    for col in range(1, 9):
        max_length = max(len(str(cell.value)) if cell.value else 0 for cell in hoja[get_column_letter(col)])
        hoja.column_dimensions[get_column_letter(col)].width = max_length + 2

    wb.save(archivo_excel)
    return "Archivo guardado correctamente."