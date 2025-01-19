from datetime import datetime

def verificar_clase_profesor(hoja, profesor, dia, empieza, termina):
    """
    Verifica si el profesor tiene clases asignadas en el mismo horario en otra aula.
    """
    hora_inicio = datetime.strptime(empieza, "%H:%M")
    hora_termina = datetime.strptime(termina, "%H:%M")
    
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    columna_dia = dias.index(dia) + 2  # Asume que los días están indexados en las columnas empezando desde la columna 2
    
    for i in range(2, hoja.max_row + 1):  # Recorre las filas desde la fila 2
        cell = hoja.cell(row=i, column=columna_dia)
        profesor_cell = hoja.cell(row=i, column=1)  # Asume que el nombre del profesor está en la columna 1
        
        if profesor_cell.value == profesor and cell.value:
            # Si el profesor ya tiene una clase asignada ese día
            horario = cell.value.split(" - ")
            try:
                curso_inicio = datetime.strptime(horario[1].split()[0], "%H:%M")
                curso_termina = datetime.strptime(horario[1].split()[1], "%H:%M")
            except (IndexError, ValueError):
                continue
            
            # Si hay un solapamiento de horarios
            if hora_inicio < curso_termina and hora_termina > curso_inicio:
                return f"Conflicto: El profesor {profesor} ya tiene una clase asignada en ese horario.", False

    return "", True

def verificar_conflicto(hoja, curso, dia, empieza, termina, salon, profesor):
    """
    Verifica si hay un conflicto con el aula o el profesor.
    """
    # Verificar conflictos de aula
    mensaje_aula, continuar_aula = verificar_conflicto_aula(hoja, dia, empieza, termina, salon)
    
    if not continuar_aula:
        return mensaje_aula, False

    # Verificar si el profesor tiene clases en otra aula
    mensaje_profesor, continuar_profesor = verificar_clase_profesor(hoja, profesor, dia, empieza, termina)
    
    if not continuar_profesor:
        return mensaje_profesor, False

    return "", True

def verificar_conflicto_aula(hoja, dia, empieza, termina, salon):
    """
    Verifica si hay un conflicto en el uso del aula.
    """
    hora_inicio = datetime.strptime(empieza, "%H:%M")
    hora_termina = datetime.strptime(termina, "%H:%M")
    
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    columna_dia = dias.index(dia) + 2  # Asume que los días están indexados en las columnas empezando desde la columna 2
    
    for i in range(2, hoja.max_row + 1):  # Recorre las filas desde la fila 2
        cell = hoja.cell(row=i, column=columna_dia)
        
        if cell.value and salon in cell.value:
            # Si el aula ya tiene una clase asignada
            horario = cell.value.split(" - ")
            try:
                curso_inicio = datetime.strptime(horario[1].split()[0], "%H:%M")
                curso_termina = datetime.strptime(horario[1].split()[1], "%H:%M")
            except (IndexError, ValueError):
                continue
            
            # Si hay un solapamiento de horarios
            if hora_inicio < curso_termina and hora_termina > curso_inicio:
                return f"Conflicto: El aula {salon} ya está ocupada en ese horario.", False

    return "", True

def asignar_salon(hoja, curso, dia, empieza, termina, profesor):
    """
    Intenta asignar un aula disponible para el curso. Verifica conflictos de aulas y profesores.
    """
    # Lista de aulas disponibles
    aulas = ["Aula 1", "Aula 2", "Aula 3"]
    
    # Buscar la primera aula disponible
    for salon in aulas:
        mensaje_conflicto, continuar = verificar_conflicto(hoja, curso, dia, empieza, termina, salon, profesor)
        if continuar:
            # Asignar el curso a esta aula
            guardar_en_excel(curso, dia, empieza, termina, salon, profesor)
            return f"Clase asignada en {salon}"
    
    return "No se pudo asignar ninguna aula"

def guardar_en_excel(curso, dia, empieza, termina, salon, profesor):
    """
    Función para guardar los datos en el archivo Excel.
    """
    # Esta función debe ser implementada según las necesidades específicas
    print(f"Guardando: {curso}, {dia}, {empieza}-{termina}, {salon}, {profesor}")
