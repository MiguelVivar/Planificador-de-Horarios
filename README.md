# Planificador de Aulas y Horarios de Clases

## Descripción
Esta es una aplicación diseñada para facilitar la planificación y organización de horarios de clases en instituciones educativas. Permite optimizar el uso de aulas y recursos, asegurando que no haya conflictos en los horarios. Además, ofrece una interfaz gráfica amigable y funcional, con la posibilidad de exportar los datos en formato Excel, con tablas visualmente organizadas y coloreadas para mejorar la legibilidad.

---

## Características
- **Interfaz gráfica intuitiva**: Diseñada con `Tkinter` para facilitar la interacción del usuario.
- **Validación de datos**: Verifica que los datos ingresados sean correctos y estén completos.
- **Detección de conflictos**: Revisa los horarios para evitar conflictos de espacio y tiempo en las aulas.
- **Exportación a Excel**: Guarda los horarios en un archivo Excel con un formato limpio y profesional.
- **Compatibilidad con horarios complejos**: Manejo de múltiples aulas, días y horarios con gran precisión.

---

## Requisitos

### Tecnologías
- Python 3.8+
- Librerías adicionales:
  - `tkinter`: Para la creación de la interfaz gráfica.
  - `openpyxl`: Para la manipulación de archivos Excel.

### Instalación de librerías
Asegúrate de instalar las librerías necesarias ejecutando:
```bash
pip install openpyxl
```

---

## Estructura del Proyecto
```
Planificador-de-Horarios/
├── main.py                # Archivo principal de la aplicación
├── gui/
│   └── interfaz.py        # Módulo para la interfaz gráfica
├── modules/
│   └── excel.py           # Funciones para guardar datos en Excel
└── README.md              # Documentación del proyecto
```

---

## Uso

1. Ejecuta el archivo principal:
   ```bash
   python main.py
   ```

2. Cargar el archivo excel con los datos. Haciendo click en el bóton **Cargar datos**. El excel debe tener la siguiente estructura:
   - Hoja "Ciclos":

      - Columna 1: Ciclo (Ejemplo: I, II, III, ..., X)
      - Columna 2: Estudiantes inscritos (Número de estudiantes)
      - Columna 3: Turno (Mañana o Tarde)

   - Hoja "Salones":

      - Columna 1: Salón (Ejemplo: A101, A102, ...)
      - Columna 2: Capacidad (Número de personas)

   - Hoja "Turno":

      - Columna 1: Turno (Mañana o Tarde)
      - Columna 2: Hora de inicio
      - Columna 3: Hora de fin

   - Hoja "Cursos":

      - Columna 1: Curso (Nombre del curso)
      - Columna 2: Ciclo (I, II, III, ...)
      - Columna 3: Horas de teoría
      - Columna 4: Horas de prácticas
      - Columna 6: Código del curso

   - Hoja "Profesores":

      - Columna 1: Profesor (Nombre del profesor)
      - Columna 2: Cursos (Lista de cursos que el profesor puede enseñar, correspondiente a diferentes ciclos)

3. Completa todos los campos.

4. Haz clic en el botón **Generar horarios**:
   - Si hay un conflicto, se mostrará un mensaje de error en la interfaz.
   - Si los datos son válidos, el horario será guardado en el archivo Excel.

5. Los datos serán exportados automáticamente en un archivo Excel organizado. Puedes abrir el directorio dónde se guarda dando click al bóton **Ver Horarios**:

---

## Contribución
Para mejorar o cambiar, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad (`git checkout -b nueva-funcionalidad`).
3. Realiza tus cambios y haz un commit (`git commit -m "Añadida nueva funcionalidad"`).
4. Haz un push a tu rama (`git push origin nueva-funcionalidad`).
5. Abre un pull request.

---

## Autores
**Miguel Vivar**   
GitHub: [MiguelVivar](https://github.com/MiguelVivar)

**Mario Muñoz**   
GitHub: [ChuchiPr](https://github.com/ChuchiPr) 

**Luis Mitma**   
GitHub: [Elextranjero1942](https://github.com/Elextranjero1942) 

**Angielina Soto**   
GitHub: [Rinvinvin](https://github.com/Rinvinvin)

**Rodrigo Conislla**   
GitHub: [Rodri2505](https://github.com/Rodri2505)

**Juan Ttito**   
GitHub: [juanttito1003](https://github.com/juanttito1003)

**Anthony Palomino** 
GitHub: [DaPcxD](https://github.com/DaPcxD)