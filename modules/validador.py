from datetime import datetime

def validar_datos(curso, profesor):
    CONTINUAR = True
    mensaje = ""

    if curso == "":
        mensaje = "Nombre de curso no válido"
        CONTINUAR = False

    if CONTINUAR:
        if profesor == "":
            mensaje = "Nombre de profesor no válido"
            CONTINUAR = False

    return mensaje, CONTINUAR
