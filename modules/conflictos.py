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
            
            # Verificamos si el contenido de la celda tiene un formato válido de hora
            try:
                curso_inicio = datetime.strptime(horario[1].split()[0], "%H:%M")
                curso_termina = datetime.strptime(horario[1].split()[1], "%H:%M")
            except (IndexError, ValueError):
                # Si ocurre un error al intentar convertir las horas, ignoramos esa fila
                continue
            
            # Verificamos si hay un conflicto en el horario
            if (hora_inicio < curso_termina and hora_termina > curso_inicio):
                return f"Conflicto: El aula {salon} ya está ocupada en ese horario.", False

    return "", True