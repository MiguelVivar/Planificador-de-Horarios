from datetime import datetime

def verificar_conflicto(hoja, curso, dia, empieza, termina, salon):
    hora_inicio = datetime.strptime(empieza, "%H:%M")
    hora_termina = datetime.strptime(termina, "%H:%M")
    
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    columna_dia = dias.index(dia) + 2
    
    for i in range(2, hoja.max_row + 1):
        cell = hoja.cell(row=i, column=columna_dia)
        
        if cell.value and salon in cell.value:
            horario = cell.value.split(" - ")
            try:
                curso_inicio = datetime.strptime(horario[1].split()[0], "%H:%M")
                curso_termina = datetime.strptime(horario[1].split()[1], "%H:%M")
            except (IndexError, ValueError):
                continue
            
            if (hora_inicio < curso_termina and hora_termina > curso_inicio):
                return f"Conflicto: El aula {salon} ya está ocupada en ese horario.", False

    return "", True

def asignar_salon(hoja, curso, dia, empieza, termina):
    # Lista de aulas disponibles
    aulas = ["Aula 1", "Aula 2", "Aula 3"]
    
    # Buscar la primera aula disponible
    for salon in aulas:
        mensaje_conflicto, CONTINUAR = verificar_conflicto(hoja, curso, dia, empieza, termina, salon)
        if CONTINUAR:
            # Asignar el curso a esta aula
            guardar_en_excel(curso, dia, empieza, termina, salon)
            return f"Clase asignada en {salon}"
    
    return "No se pudo asignar ninguna aula"